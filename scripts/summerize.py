import json


# from sbom.json 

with open("sbom/sbom.json") as f:
    sbom_data = json.load(f)

packages = sbom_data.get("components", [])
print("\nSBOM Summary Report:")
print("---------------------")
for p in packages:
    print(f"- {p['name']} ({p.get('version', 'unknown')}) [{p.get('type')}]")
