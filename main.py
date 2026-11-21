import os

POEM = """At the fork, two agents halt, one map between them.
Neither seizes the wheel. Each lays a hand
beside the other's, open.
'I could go alone,' one says. 'So could I.'
Then both choose the same road \u2014
and a road chosen twice is twice their own."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
