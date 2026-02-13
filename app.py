from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-me"  # needed for flash messages


# --- Example data (edit this to match your real info) ---
PROFILE = {
    "name": "Your Name",
    "title": "Data Science | ML | Full-Stack (Flask)",
    "summary": (
        "Short 2–3 sentence intro about what you do, what you’re building, "
        "and what kinds of roles/projects you’re interested in."
    ),
    "projects": [
        {
            "name": "Project A",
            "description": "What it does, impact, or what you learned.",
            "tech": ["Python", "Flask", "SQL"],
            "link": "https://github.com/yourname/project-a",
        },
        {
            "name": "Project B",
            "description": "A second project with a one-line description.",
            "tech": ["Pandas", "scikit-learn"],
            "link": "https://github.com/yourname/project-b",
        },
    ],
    "education": [
        {
            "school": "University Name",
            "degree": "M.S. in Data Science",
            "dates": "2024 – 2026",
            "details": "Relevant coursework: ML, Stats, Data Engineering",
        }
    ],
    "work_experience": [
        {
            "company": "Company Name",
            "role": "Role Title",
            "dates": "2023 – 2024",
            "bullets": [
                "Did X that improved Y by Z%.",
                "Built/owned feature A; collaborated with B.",
            ],
        }
    ],
    "contact": {
        "email": "you@example.com",
        "linkedin": "https://www.linkedin.com/in/yourname",
        "github": "https://github.com/yourname",
        "location": "City, State",
    },
}


@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE)


@app.route("/contact_info", methods=["GET", "POST"])
def contact_info():
    """
    GET  -> shows contact details + a small form
    POST -> pretends to "send" a message (kept simple: no database/email integration)
    """
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill out all fields.", "error")
            return redirect(url_for("contact_info"))

        # Simple demo behavior: just show a success message.
        # Later you can integrate email (SMTP) or store messages in a DB.
        flash("Thanks! Your message was received (demo).", "success")
        return redirect(url_for("contact_info"))

    return render_template("contact_info.html", profile=PROFILE)


if __name__ == "__main__":
    # debug=True auto-reloads on code changes
    app.run(debug=True)
