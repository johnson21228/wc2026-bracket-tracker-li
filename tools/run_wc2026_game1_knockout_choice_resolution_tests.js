#!/usr/bin/env node
/*
Run Game 1 knockout choice resolution tests without a browser.

This script extracts the installed WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS
script from site/game1/index.html, evaluates it in a minimal Node VM window, and
runs deterministic seeded fixtures for R16, QF, and SF contestant resolution.

It also loads site/data/game1_data_bundle.js before evaluating the page harness,
because the installed Game 1 harness expects the same WC2026_GAME1_DATA global
that the browser receives from the data bundle script tag.
*/
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = process.cwd();
const GAME1 = path.join(ROOT, 'site', 'game1', 'index.html');
const DATA_BUNDLE = path.join(ROOT, 'site', 'data', 'game1_data_bundle.js');
const MARKER = 'WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS';

function fail(message) {
  console.error(`ERROR: ${message}`);
  process.exit(1);
}

function assert(condition, message) {
  if (!condition) fail(message);
}

function extractHarnessScript(html) {
  const markerIndex = html.indexOf(MARKER);
  if (markerIndex < 0) fail(`missing ${MARKER} in site/game1/index.html`);

  const scriptStart = html.lastIndexOf('<script', markerIndex);
  const openEnd = html.indexOf('>', scriptStart);
  const scriptEnd = html.indexOf('</script>', markerIndex);

  if (scriptStart < 0 || openEnd < 0 || scriptEnd < 0 || scriptEnd < openEnd) {
    fail('could not extract knockout choice resolution harness <script> block');
  }
  return html.slice(openEnd + 1, scriptEnd);
}

function createVmContext() {
  const window = {};
  window.window = window;

  const document = {
    querySelector() { return null; },
  };

  return vm.createContext({
    window,
    document,
    console,
    Error,
    Object,
    Array,
    String,
    Number,
    RegExp,
    Set,
    Map,
  });
}

function loadGame1DataBundle(context) {
  if (!fs.existsSync(DATA_BUNDLE)) {
    fail(`missing ${DATA_BUNDLE}; Game 1 Node knockout tests require the generated data bundle`);
  }

  const source = fs.readFileSync(DATA_BUNDLE, 'utf8');
  try {
    vm.runInContext(source, context, { filename: 'site/data/game1_data_bundle.js' });
  } catch (error) {
    fail(`failed evaluating site/data/game1_data_bundle.js in Node VM: ${error && error.stack ? error.stack : error}`);
  }

  if (!context.window.WC2026_GAME1_DATA) {
    fail('site/data/game1_data_bundle.js evaluated, but window.WC2026_GAME1_DATA was not installed');
  }

  // Some extracted page snippets look up GAME1_DATA as a global binding, while
  // others read window.WC2026_GAME1_DATA. Provide both in the VM.
  context.GAME1_DATA = context.window.WC2026_GAME1_DATA;
}

function team(id, name, group) {
  return { id, name, abbr: id, group };
}

function choiceLabels(result) {
  return result.contestants.map((t) => `${t.name || t.display || t.id} (${t.abbr || t.id})`);
}

function expectTwo(testName, result, expectedFeeders) {
  assert(result, `${testName}: no result returned`);
  assert(Array.isArray(result.feeders), `${testName}: result.feeders is not an array`);
  assert(Array.isArray(result.contestants), `${testName}: result.contestants is not an array`);
  assert(result.feeders.join(',') === expectedFeeders.join(','), `${testName}: feeders ${result.feeders.join(',')} did not match ${expectedFeeders.join(',')}`);
  assert(result.contestants.length === 2, `${testName}: expected exactly two contestants; got ${result.contestants.length}`);
  assert(result.contestants.every((t) => t && (t.id || t.name || t.display)), `${testName}: contestant missing id/name/display`);
  return {
    testName,
    slotId: result.slotId,
    feeders: result.feeders,
    choices: choiceLabels(result),
    ok: true,
  };
}

function main() {
  if (!fs.existsSync(GAME1)) fail(`missing ${GAME1}; run from repo root`);
  const html = fs.readFileSync(GAME1, 'utf8');
  const harnessScript = extractHarnessScript(html);
  const context = createVmContext();

  loadGame1DataBundle(context);

  try {
    vm.runInContext(harnessScript, context, { filename: 'site/game1/index.html:knockout-choice-tests' });
  } catch (error) {
    fail(`failed evaluating knockout choice test harness in Node VM: ${error && error.stack ? error.stack : error}`);
  }

  const api = context.window.WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS;
  assert(api, 'test harness did not install window.WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS');
  assert(typeof api.resolveKnockoutChoiceContestants === 'function', 'missing resolveKnockoutChoiceContestants function');
  assert(typeof api.testKnockoutChoiceResolution === 'function', 'missing testKnockoutChoiceResolution function');

  const results = [];

  // R16: choices are the two teams assigned to the two feeding R32 slots.
  context.window.game1R32Picks = {
    'R32-1': team('CAN', 'Canada', 'B'),
    'R32-2': team('QAT', 'Qatar', 'B'),
    'R32-3': team('BRA', 'Brazil', 'C'),
    'R32-4': team('SCO', 'Scotland', 'C'),
  };
  context.window.game1KnockoutPicks = {};
  results.push(expectTwo('R16-1 from R32-1/R32-2', api.testKnockoutChoiceResolution('R16-1'), ['R32-1', 'R32-2']));
  results.push(expectTwo('R16-2 from R32-3/R32-4', api.testKnockoutChoiceResolution('R16-2'), ['R32-3', 'R32-4']));

  // QF: choices are the two picked R16 winners.
  context.window.game1KnockoutPicks = {
    'R16-1': team('CAN', 'Canada', 'B'),
    'R16-2': team('BRA', 'Brazil', 'C'),
  };
  results.push(expectTwo('QF-1 from R16-1/R16-2', api.testKnockoutChoiceResolution('QF-1'), ['R16-1', 'R16-2']));

  // SF: choices are the two picked QF winners.
  context.window.game1KnockoutPicks = {
    'QF-1': team('CAN', 'Canada', 'B'),
    'QF-2': team('GER', 'Germany', 'E'),
  };
  results.push(expectTwo('SF-1 from QF-1/QF-2', api.testKnockoutChoiceResolution('SF-1'), ['QF-1', 'QF-2']));

  console.log(JSON.stringify({
    ok: true,
    dataBundleLoaded: Boolean(context.window.WC2026_GAME1_DATA),
    dataBundleVersion: context.window.WC2026_GAME1_DATA.version || null,
    results,
  }, null, 2));
}

main();
