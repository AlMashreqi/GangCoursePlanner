from itertools import combinations

def normalize_courses(course_string):
    """Convert 'Course1, Course2' → set(['Course1', 'Course2'])"""
    return set(course.strip() for course in course_string.split(","))


def find_common_courses(students):
    course_sets = {
        name: normalize_courses(courses)
        for name, courses in students.items()
    }

    names = list(course_sets.keys())

    for r in range(2, len(names) + 1):
        print(f"\n--- Groups of {r} ---")
        for group in combinations(names, r):
            # Intersection of all courses in the group
            common = set.intersection(
                *(course_sets[name] for name in group)
            )

            if common:
                group_name = " & ".join(group)
                courses = ", ".join(sorted(common))
                print(f"{group_name} can take the following courses together: {courses}")


students = {
    "Abrar": "QRMT, POS, GB, L&W, M&B",
    "Saud": "QRMT, M&B, IC, GB, EVS, L&W",
    "Pulkit": "QRMT, GB, EVS, L&W, POS"
}

find_common_courses(students)