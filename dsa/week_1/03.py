emp_data = [input(f"Enter Id of Employee {i+1}: ") for i in range(int(input("Number of employees: ")))] 
def search_for_emp(li, id, n):
    if li[n] == id:
        print(f"id found at index: {n}")
        return

    if n >= len(li) - 1:
        print(f"id not found: {n}")
        return

    return search_for_emp(li, id, n+1)
to_search = input("id to search for: ")
search_for_emp(emp_data, to_search, 0)
