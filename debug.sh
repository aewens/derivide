#!/bin/bash

uvicorn app:app --port $1 --reload
