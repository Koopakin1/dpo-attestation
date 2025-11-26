# DPO Attestation Project

This project implements a system for DPO (Additional Professional Education) attestation with partner and exam bots.

## Features

- Partner bot for course creation and management
- Exam bot for student assessment
- AI-powered course content generation
- Diploma generation and management
- Referral system
- Bonus system for partners

## Architecture

The system consists of two separate bots:

1. **Partner Bot**: For course creation and partner management
2. **Exam Bot**: For student examination and diploma issuance

Both bots use SQLite for FSM state storage and PostgreSQL for persistent data.

## Setup

1. Install dependencies from requirements.txt
2. Set up environment variables in .env
3. Run the bots separately

## Technologies

- Python 3.11
- Aiogram 3
- PostgreSQL
- SQLAlchemy
- ReportLab
- Anthropic API
