---
title:
author:
track: api-security | ai-security
difficulty: intermediate | advanced
language: en
description:
---

# Title

> **WARNING: This lab is deliberately vulnerable. Do not deploy it to any
> network. Run it locally or in an isolated sandbox only.**

## Overview

What vulnerability or concept does this lab demonstrate?

## Learning objectives

- Objective 1
- Objective 2

## Prerequisites

- Docker and Docker Compose installed
- Basic knowledge of ...

## Setup

```bash
docker-compose up --build
```

```yaml
# docker-compose.yml
version: "3.8"
services:
  vulnerable-app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - NODE_ENV=development
```

## The vulnerability

Explain what is vulnerable and why.

## Exploitation steps

Step-by-step instructions for the learner.

## SOLUTION.md

<!-- Create a separate SOLUTION.md file with the full walkthrough. -->

See [SOLUTION.md](SOLUTION.md) for the complete solution.

## How to fix it

Explain the correct remediation.

## Cleanup

```bash
docker-compose down -v
```
