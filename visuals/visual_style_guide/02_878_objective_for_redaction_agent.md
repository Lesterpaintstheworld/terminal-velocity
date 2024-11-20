## Objective for Redaction Agent
1. **Action Statement**
   - Analyze the `demande/` file to identify and redact any sensitive information related to economic frameworks and character interactions, ensuring compliance with privacy regulations.

### Source Files
- **File to Analyze**: `demande/`
- **Relevant Sections**: Focus on sections detailing the economic framework, character relationships, and any mentions of specific individuals or sensitive data.
- **Dependencies**: Ensure access to the database of sensitive data types for reference during the redaction process.

2. **Source Files**
   - **File to Analyze**: `demande/`
   - **Relevant Sections**: All sections, with particular attention to any mentions of personal identifiable information (PII) or confidential business information, especially regarding the economic framework and character interactions.

3. **Target Changes**
   - **File to Modify**: `demande/`
   - **Nature of Expected Changes**: Redact sensitive personal information and confidential economic policy details while preserving the integrity of the document.
   - **Impact on System State**: The document will be compliant with privacy regulations and organizational policies post-redaction.

4. **Validation Points**
   - **How to Verify Success**: Review the final output to confirm no residual sensitive information is visible.
   - **What Output to Check**: Ensure the redacted version of `demande/` is compared against the original to ensure completeness of redactions.
   - **Which States to Validate**: Confirm that the redaction process logs show no errors and that the output meets the defined quality standards.

5. **Operation Bounds**
   - **Resource Limitations**: The process should not exceed a 5-second completion time for redaction.
   - **Scope Restrictions**: Focus solely on redaction; do not engage in marketing strategies or user testing.
   - **Dependency Requirements**: Ensure access to the secure storage for original and redacted documents.

6. **Search**
   - No search required.

```
