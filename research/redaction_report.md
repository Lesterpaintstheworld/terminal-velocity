## Objective for Redaction Agent
1. **Action Statement**
   - Review and redact sensitive information in the `research/redaction_report.md` file to ensure compliance with privacy regulations and maintain document integrity.

## Objective for Redaction Agent

### Action Statement
Conduct a thorough review of the `demande.md` file to identify and redact any sensitive information related to the economic framework and character interactions that could violate privacy regulations. Ensure that the enhanced redaction protocols for economic data are applied consistently throughout the document.

### Source Files
- **File to Analyze**: `demande.md`
- **Relevant Sections**: Focus on sections detailing the economic framework, character relationships, and any mentions of specific individuals or sensitive data.
- **Dependencies**: Ensure access to the database of sensitive data types for reference during the redaction process.

2. **Source Files**
   - Analyze the `research/redaction_report.md` file.
   - Relevant sections include the entire document as it outlines sensitive information that may need redaction.

3. **Target Changes**
   - Modify the `research/redaction_report.md` file by redacting any sensitive economic data and character interaction details.
   - The expected changes should clear out any confidential information while maintaining the overall structure and purpose of the document.
- **Impact on System State**: The document should be compliant with privacy regulations, ensuring that all sensitive data is securely handled and removed.

4. **Validation Points**
   - Verify success by ensuring no sensitive information remains visible in the `research/redaction_report.md` file.
   - Check that the redacted document maintains its integrity and clarity for future use.

5. **Operation Bounds**
   - Resource limitations: Ensure the redaction process is completed within 2 hours due to potential time constraints for document usage.
   - Scope restrictions: Focus solely on redaction; no alterations to document structure or additional content creation.
   - Dependency requirements: The operation requires access to the sensitive data types database to effectively identify what needs to be redacted.

6. **Search:** 
   - Search: "sensitive economic data" in `research/redaction_report.md` to identify specific sections requiring redaction.
