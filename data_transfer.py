#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "indbuy.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


from search_api.models import CuniqueData
import pandas as pd
#
df = pd.read_csv('statics_data/cunique.csv')


CuniqueData.objects.all().delete()
print("clearing db first")
for r in range(len(df)):
    print(r)
    # if r == 100:
    #     break
    row = df.iloc[r]
    CuniqueData.objects.create(
        message=row['Message'],
        truth=row['truth'],
        cube=row['cube'],
        google=row['google'],
        ibm=row['ibm'],
        google_spam=float(row['google_spam']),
        google_not_spam=float(row['google_not_spam']),
        ibm_spam=float(row['ibm_spam']),
        ibm_not_spam=float(row['ibm_not_spam'])
    )

print("Done all")
