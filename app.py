from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-me"  # needed for flash messages


# --- Resume-driven content (edit anytime) ---
PROFILE = {
    "name": "Ziheng (Tony) Fang",
    "headline": "M.S. Data Science (SJSU) | Former Software Developer (MGM Resorts) | Seeking Internship",
    "location": "San Jose, CA 95112",
    "citizenship": "US Citizen",
    "summary": (
        "Former full-time software developer currently pursuing an M.S. in Data Science at San Jose State University. "
        "Seeking an internship. Strong CS fundamentals and hands-on experience with AI/ML topics, reinforcement learning, "
        "and SQL databases."
    ),
    "skills": {
        "AI/ML": [
            "Machine Learning",
            "Neural Networks",
            "Reinforcement Learning",
            "Clustering / Cluster Analysis",
        ],
        "CS Foundations": ["Search Algorithms", "Game Theory", "Probability", "Mathematical Statistics", "Combinatorics"],
        "Programming": ["Python", "Java", "C++", "C#"],
        "Backend & Cloud": ["Spring Boot", "Maven", "Azure DevOps", "CircleCI", "AWS", "CI/CD", "Unit/Integration Testing"],
        "Data": ["SQL Databases"],
    },
    "education": [
        {
            "school": "San Jose State University",
            "degree": "M.S. Data Science",
            "dates": "Fall 2024 – Present",
            "details": [
                "GPA: 3.4",
                "Courses: Artificial Intelligence, Topics in ML, Reinforcement Learning, Probability Theory, Cluster Analysis, "
                "Mathematical Statistics, Database Management, Web Intelligence, Data Visualization",
                "Thesis: Choosing the number of clusters and the fuzzifier exponent in fuzzy clustering",
            ],
        },
        {
            "school": "University of Nevada, Las Vegas",
            "degree": "B.S. Computer Science, Minor in Mathematics",
            "dates": "Graduated Dec 2020",
            "details": [
                "GPA: 3.57",
                "Dean’s List: Fall 2019, Spring 2020",
            ],
        },
    ],
    "experience": [
        {
            "company": "MGM Resorts Int’l — Payments Team",
            "role": "Software Developer I",
            "dates": "Feb 2021 – May 2023",
            "highlights": [
                "Developed cloud-based microservices handling 200K+ transactions/month.",
                "Tech: Java, C#, Maven, Spring Boot, Azure, CircleCI, AWS.",
                "Wrote unit + integration tests; created Postman tests for endpoints.",
                "Built/designed CI/CD pipelines using Azure DevOps and CircleCI.",
                "Deployed applications to Apigee via CircleCI and Azure DevOps.",
                "Provided on-call support for production issues with 5-minute acknowledgment standard.",
            ],
        }
    ],
    "projects": [
        # Your resume excerpt didn’t list projects explicitly.
        # Add projects here when ready; the page will render them automatically.
        # Example:
        # {"name": "Project Name", "description": "...", "tech": ["Python", "Flask"], "link": "https://..."}
    ],
    "contact": {
        "email": "tony46711@gmail.com",
        "phone": "(925) 382-2119",
        "github": "https://github.com/TFang96",
        "linkedin": "",  # add if you want; page hides empty links
    },
}


@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE)


@app.route("/contact_info", methods=["GET", "POST"])
def contact_info():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill out all fields.", "error")
            return redirect(url_for("contact_info"))

        # Keep it simple for now: just confirm receipt (no email/DB).
        flash("Thanks, Tony will get your message (demo).", "success")
        return redirect(url_for("contact_info"))

    return render_template("contact_info.html", profile=PROFILE)


if __name__ == "__main__":
    app.run(debug=True)
