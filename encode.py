

def encode(strs: list[str]) -> str:
    if not strs:
        return ""
    return "_".join(strs)


def decode(s: str) -> list[str]:
    if not s:
        return []

    return s.split("_")


strs = []

encoded_str = encode(strs)

print("Encoded:", encoded_str)

dencoded_str = decode(encoded_str)

print("Decoded:", dencoded_str)
