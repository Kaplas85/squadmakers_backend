# Python
from typing import List

# FastAPI
from fastapi import APIRouter, Query

router = APIRouter(prefix="/math", tags=["Math"])


@router.get(path="/sum/")
async def sum_one_a_number(number: float = Query(...)):
    """
    Simply, n + 1
    """
    return {"number": number, "result": number + 1}


@router.get(path="/lcm/")
async def calc_lcm(numbers: List[int] = Query(...)):
    """
    Calculate the L.C.M from a integer number list
    """
    max_value: int = max(numbers)

    while True:
        results_list: list = []
        for number in numbers:
            results_list.append(max_value % number)

        if sum(results_list) == 0:
            return {"lcm": max_value}

        max_value += 1
