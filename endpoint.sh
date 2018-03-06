#!/bin/bash

curl -X POST '0.0.0.0:8000/api/csv/' -d MOCK_DATA.csv --header "Content-Disposition: attachment; filename=MOCK_DATA.csv"