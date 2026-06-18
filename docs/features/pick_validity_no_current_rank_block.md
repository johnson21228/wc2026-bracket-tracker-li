# Pick validity: no current-rank warning

The picked-cell validity layer preserves user intent and warns only for structural conflicts. It does not mark a pick invalid simply because the current standings snapshot places the team in a rank other than the slot label.

For example, if a Group A runner-up slot offers all Group A teams, the user may pick any Group A team. The standings panel can show the current order, but the picked cell should not show a red warning merely because that team is currently first, third, or fourth.

The source-scope boundary remains intact:

- Group winner and runner-up slots are limited to their encoded group.
- Third-place candidate slots are limited to their encoded candidate group set.
- Knockout slots are limited to their feeder path.

Warnings remain useful for conflicts such as duplicate Round-of-32 team assignments or a team outside the slot's source scope.
