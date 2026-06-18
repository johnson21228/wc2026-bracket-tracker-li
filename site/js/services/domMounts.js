function requireElementById(id, documentRef = document) {
  const element = documentRef.getElementById(id);
  if (!element) {
    throw new Error(`Missing required DOM mount: #${id}`);
  }
  return element;
}

export { requireElementById };
