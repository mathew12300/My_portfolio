import json
from pathlib import Path
from django.shortcuts import render
from django.http import Http404

# App directory (portfolio/)
APP_DIR = Path(__file__).resolve().parent


# ---------- JSON LOADER ----------
def load_json(filename):
    try:
        with open(APP_DIR / "data" / filename, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] {filename} not found in portfolio/data/")
        return []
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {filename}: {e}")
        return []


# ---------- PAGES ----------
def home(request):
    profile = load_json("profile.json")
    return render(request, "portfolio/home.html", {
        "profile": profile
    })


def projects(request):
    projects = load_json("projects.json")
    return render(request, "portfolio/projects.html", {
        "projects": projects
    })


def skills(request):
    skills = load_json("skills.json")
    return render(request, "portfolio/skills.html", {
        "skills": skills
    })


def experience(request):
    experiences = load_json("experience.json")
    return render(request, "portfolio/experience.html", {
        "experiences": experiences
    })


def contact(request):
    profile = load_json("profile.json")
    return render(request, "portfolio/contact.html", {
        "profile": profile
    })


# ---------- PROJECT DETAIL ----------
def project_detail(request, slug):
    projects = load_json("projects.json")

    project = next((p for p in projects if p.get("slug") == slug), None)

    if not project:
        raise Http404("Project not found")

    return render(request, "portfolio/details.html", {
        "project": project
    })
