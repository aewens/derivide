#!/bin/bash

env/bin/uvicorn app:app --port $1 --reload
