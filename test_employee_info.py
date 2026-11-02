import employee_info as data

def test_get_employee_by_range():
    result = data.get_employees_by_age_range(20,30)

    assert len(result) == 2


def test_calculate_average_salary():
    result = data.calculate_average_salary()

    assert result == 60166.67

def test__employees_by_dept():
    result=[]
    result = data.get_employees_by_dept("Marketing")

    assert result ==[ {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]