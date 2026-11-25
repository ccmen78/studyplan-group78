"""
StudyPlan - Python API demo for AI agents.

Run:
    python demo.py

Dates are calculated from today, so the output is always valid.
Everything is local; nothing is sent to a server.
"""

from datetime import date, timedelta

import studyplan
from studyplan.storage import DATA_FILE

TODAY = date.today()


def day(offset: int) -> str:
    """Return an ISO date string N days from today."""
    return (TODAY + timedelta(days=offset)).isoformat()


def section(title: str) -> None:
    line = "=" * 58
    print(f"\n{line}\n{title}\n{line}")


def main() -> None:
    print(f"StudyPlan demo | today = {TODAY.isoformat()}")

    # ------------------------------------------------------------------
    section("1) GPA - credit-weighted, not a simple average")
    courses = [
        {"name": "Calculus", "credits": 4, "grade": "A"},
        {"name": "Accounting", "credits": 3, "grade": "B+"},
    ]
    gpa = studyplan.calculate_gpa(courses)
    print(f"  Courses: {courses}")
    print(f"  GPA: {gpa}")
    print("  (4 x 4.0 + 3 x 3.3) / 7 = 3.70")
    print("  A 4-credit A counts more than a 3-credit B+.")

    # ------------------------------------------------------------------
    section("2) Study plan - deadline-first with a time budget")
    tasks = [
        {"name": "Math Homework",  "due_date": day(3),  "est_minutes": 60,  "priority": "Medium"},
        {"name": "CS1302 Project", "due_date": day(7),  "est_minutes": 120, "priority": "High"},
        {"name": "Essay Draft",    "due_date": day(15), "est_minutes": 90,  "priority": "Low"},
    ]
    plan = studyplan.suggest_study_plan(tasks, available_minutes=150)
    for item in plan:
        print(f"  - {item['task_name']:<16} due {item['due_date']}  "
              f"{item['allocated_minutes']:>3} min")
    total = sum(item["allocated_minutes"] for item in plan)
    print(f"  {'TOTAL':<18} {'':<10}  {total:>3} min")
    print("  Earliest deadline is funded first. The 120-min project gets the")
    print("  remaining 90 min; the essay gets 0, so it does not appear.")

    # ------------------------------------------------------------------
    section("3) Deadline urgency - three bands")
    for offset in (3, 7, 15):
        deadline = day(offset)
        print(f"  {deadline}: {studyplan.days_left(deadline):>2} days left"
              f" -> {studyplan.urgency_level(deadline)}")
    print("  0-3 days = High, 4-7 = Medium, 8+ = Low.")

    # ------------------------------------------------------------------
    section("4) Exam countdown")
    exam = day(25)
    print(f"  Exam on {exam}: {studyplan.exam_countdown(exam)} days remaining")

    # ------------------------------------------------------------------
    section("5) Quiz generator - structured cards")
    notes = {
        "Demand": "Relationship between price and quantity demanded",
        "Accounts Receivable": "Money owed by customers",
    }
    for card in studyplan.create_quiz(notes):
        print(f"  Q: {card['question']}")
        print(f"  A: {card['answer']}")

    # ------------------------------------------------------------------
    section("6) Study timer")
    session = studyplan.StudySession()
    for minutes in (45, 30, 45):
        session.add_time(minutes)
    print(f"  Minutes: {session.total_minutes()}   Hours: {session.total_hours()}")

    # ------------------------------------------------------------------
    section("7) Local-first storage")
    print(f"  Data file: {DATA_FILE}")
    print("  Plain JSON on disk. No account, no network, no telemetry.")
    print("  That is what makes it safe for an agent to run locally.")


if __name__ == "__main__":
    main()
