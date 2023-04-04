from fastapi import FastAPI, Body, Response, status
from parse_utils import parse_json


app = FastAPI()

@app.post("/api/script")
async def run_code(response: Response, json_data: dict = Body(...)):
    code = json_data['code']
    return_name = json_data['return_name']
    args = json_data['args']

    global_vars = {}
    local_vars = {"kwargs": args}

    try:
        exec(code, global_vars, local_vars)
    except Exception as e:
        result = str(e);
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        result = local_vars[return_name]
    return {"result": result}

@app.post("/api/data-img")
async def get_img2d(response: Response, json_data: dict = Body(...)):
    code = json_data['code']
    return_name = json_data['return_name']
    raw_data = json_data['data']


    try:
        data_dict = parse_json(raw_data)
    except KeyError as key_error:
        result = str(key_error);
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'result': result}
    except ValueError as value_error:
        result = str(value_error);
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'result': result}

    args = {"data": data_dict}

    global_vars = {}
    local_vars = {"kwargs": args}

    try:
        exec(code, global_vars, local_vars)
    except Exception as e:
        result = str(e);
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        result = local_vars[return_name]
    return {"result": result}
