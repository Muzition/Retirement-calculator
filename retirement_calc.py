#! /bin/python
def retirement_calc(name, age, retirement_age=67):
    years_to_go = retirement_age - age
    if years_to_go > 0:
        return f"{name} will be old enough to retire in {years_to_go} year(s)."
    elif years_to_go == 0:
        return f"{name} is old enough to retire this year!"
    else:
        years_to_go = abs(years_to_go)
        return f"{name} was old enough to retire {years_to_go} year(s) ago."
