# Reviewed Exclusions

This ledger records notable projects that were investigated and intentionally excluded. It prevents repeated review and makes corrections auditable.

| Project                                                     | Reviewed   | Why excluded                                                                                                                                                | Reconsider when                                                             |
| ----------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [AIOS](https://github.com/agiresearch/AIOS)                 | 2026-08-22 | The repository's LICENSE file contains only a newline, so the public implementation has no effective usage grant.                                           | A clear license is added.                                                   |
| [Claude Code](https://github.com/anthropics/claude-code)    | 2026-08-22 | The public repository contains plugins, documentation, and installers rather than the core client implementation; its license reserves modification rights. | The core implementation is published under a qualifying license.            |
| [Daytona](https://github.com/daytonaio/daytona)             | 2026-08-22 | The current default branch contains a README and assets but not the sandbox implementation represented by the repository's historical stars.                | A maintained public implementation returns to the default branch.           |
| [GitHub Copilot CLI](https://github.com/github/copilot-cli) | 2026-08-22 | The custom license permits running and limited redistribution but prohibits modification and derivative works.                                              | The implementation is released under a qualifying license.                  |
| [Multica](https://github.com/multica-ai/multica)            | 2026-08-22 | The source-available license restricts hosted services and commercial embedding, so it is not treated as an open core entry.                                | The core implementation adopts an OSI-approved license.                     |
| [Vibe Kanban](https://github.com/BloopAI/vibe-kanban)       | 2026-08-22 | The project README announces that Vibe Kanban is sunsetting.                                                                                                | Maintainers formally resume the project or identify a maintained successor. |

Generated from [`data/exclusions.json`](data/exclusions.json).
