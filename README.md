## README.md

# SBOM SecureFlow

This project demonstrates how to generate a Software Bill of Materials (SBOM), scan for vulnerabilities, and prevent deployment if high-severity CVEs are found.

## 🔧 Stack
- Syft: SBOM generation
- Grype: CVE scanning
- GitHub Actions: CI pipeline
- Python Flask app: intentionally vulnerable

## 📄 Features
- SBOM output in CycloneDX format
- Scan on every push/PR
- Block on high CVSS vulnerabilities
- CVE summary script

## 🧪 Case Studies

### Log4Shell (CVE-2021-44228)
Java logging lib (`log4j`) allowed remote code execution. Many orgs didn't know they were even using it — SBOMs help trace transitive dependencies.

### SolarWinds Supply Chain Attack
Hackers injected malware in a signed update. Shows why build-time scanning and SBOM visibility is crucial.
