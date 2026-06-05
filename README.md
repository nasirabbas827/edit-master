# edit_master_prototype  

A lightweight Django prototype that demonstrates a full‑stack workflow for managing election data, user profiles, and blockchain‑backed voting. The project is organized as a single Django app (`myapp`) and includes a series of migrations that evolve the data model from a simple profile to a complete election system with candidate pictures, PDF uploads, and blockchain integration.

---

## Overview  

`edit_master_prototype` showcases how to:

* Build a **CRUD** interface for user profiles, candidates, and elections.  
* Store immutable voting records on a **blockchain** (via a simple wrapper).  
* Manage complex migrations while evolving the data schema.  
* Leverage Django’s built‑in admin for rapid prototyping and testing.  

The codebase is intentionally minimal, making it an excellent starting point for developers who want to explore:

* Django app structure and migrations.  
* Integration of external services (e.g., blockchain APIs).  
* Basic form handling and file uploads (PDFs, candidate pictures).  

---

## Features  

| Feature | Description |
|---------|-------------|
| **User Profiles** | Create, edit, and view profiles with optional picture, address, DOB, and email fields. |
| **Election Management** | Define elections, set status (open/closed), and assign candidates. |
| **Candidate Handling** | Upload candidate pictures, associate them with elections, and manage candidate data. |
| **Blockchain Voting** | Record each vote on a blockchain to guarantee immutability and auditability. |
| **PDF Uploads** | Store supporting documents (e.g., candidate manifestos) as uploaded PDFs. |
| **Admin Interface** | Full‑featured Django admin for quick data inspection and manipulation. |
| **Migrations** | 13 incremental migrations that illustrate real‑world schema evolution. |

---

## Tech Stack  

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.9 |
| **Web Framework** | Django (≥3.2) |
| **Database** | SQLite (default) – replace with PostgreSQL/MySQL for production |
| **Blockchain** | Simple wrapper around a public blockchain API (replace with your provider) |
| **Front‑end** | Django templates (HTML) – extendable with Bootstrap, React, etc. |
| **Testing** | Django’s built‑in test runner (unit tests can be added) |
| **Version Control** | Git (GitHub) |

---

## Installation  

> **Note:** The steps below assume a Unix‑like environment (Linux/macOS). Windows users can adapt the commands accordingly.

1. **Clone the repository**  

   ```bash
   git clone https://github.com/yourusername/edit_master_prototype.git
   cd edit_master_prototype
   ```

2. **Create a virtual environment**  

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  

   The project does not ship a `requirements.txt` file