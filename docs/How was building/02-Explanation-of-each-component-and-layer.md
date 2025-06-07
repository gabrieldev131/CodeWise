---
id: 02-Explanation-of-each-component-and-layer
title: Explanation of each component and layer
sidebar_label: Explanation of each component and layer
---

## Model:
- Code validation rules.
    - Good practices
    - Style
    - Quality
    - Security
    - Performance
    - Adherence to team/project standards
- Integration with external analysis APIs, such as the Gemini API (Google), which processes and generates suggestions about the code.
- Representation of Pull Request data:
    - ID of PR
    - Author
    - List of modified files
    - File contents
    - Improvement suggestions
- Integration with agentops, for monitoring models and agents.
- Statistical calculations on the analyzed codes, analyzing errors, possible bugs, code smell, an analysis of individual and collective activity.

## View:
- Automatic comment when performing Pull Request on GitHub
- Message formatted in the Discord channel or other means of communication
- Response to a frontend API
- Format and display improvement suggestions clearly
- Adapt content to the delivery medium
- Display individual data (for each collaborator) and collective data for a project
    - Display of grades, from 0 to 5, taking into account code validation rules
- Interface for configuring:
    - API keys
    - URLs
    - Database
    - Access permissions (ex: github)

## Controller:
- Detects creation/update of Pull Requests (via GitHub Webhook or n8n)
- Sends changed code for analysis by the model
- Formats the results and forwards them to the output channels via view
