---
id: 01-Design-of-the-architecture
title: Design of the Architecture
sidebar_label: Design of the Architecture
---

**MVC ARCHITETURE**

MVC is an architecture where it is divided into 3 parts, model, view and controller

**Model:** Responsible for data and business logic. It represents Pull Request data, code analysis rules and improvement suggestions, as well as the insertion of comments in the source code.

**View:** Responsible for the user interface. This is where the panel is showing statistics, forecasts (delivery times) and where the user can enter or change the details that interest them most in the analysis.

**Controller:** Manages the interaction between the model and the View. This is when the pull request is inspected on github, sending the data to the model and showing the results in the view.
