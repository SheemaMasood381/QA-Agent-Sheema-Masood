### Creating an Interview with Job Description
**Steps:**
1. Go to the interview creation page
2. Enter a job description or use the enhanced JD feature to generate one
3. Save the job description
4. Verify that skill recommendations are displayed
**Expected Result:** Skill recommendations are displayed based on the job description

### Selecting Skills and Difficulty Level
**Steps:**
1. Select skills from the AI-suggested list or add custom skills
2. Choose a difficulty level for the questions (hard, moderate, etc.)
**Expected Result:** Skills and difficulty level are saved successfully

### Reviewing and Customizing Standard Questions
**Steps:**
1. Review the standard questions generated by the AI
2. Personalize the options for each question
3. Check the box next to a preferred answer
**Expected Result:** Standard questions are updated with customizations

### Reviewing and Customizing Role-Based Questions
**Steps:**
1. Review the role-based questions generated by the AI
2. Modify the question and ideal answer if needed
**Expected Result:** Role-based questions are updated with customizations

### Creating the Interview
**Steps:**
1. Click the 'Create' button to create the interview
**Expected Result:** The interview is created successfully and a unique public interview link is generated

### Verifying Interview Link
**Steps:**
1. Copy the public interview link
2. Verify that the link is unique and exclusive to the interview
**Expected Result:** The public interview link is valid and unique

### View candidate responses
**Steps:**
1. {'action': 'visit', 'target': '/responses'}
2. {'action': 'waitForSelector', 'target': '.candidate-response'}
**Expected Result:** Candidate responses are displayed with structured answers, video recordings, scores, and resumes.

### View detailed AI analysis scores
**Steps:**
1. {'action': 'visit', 'target': '/interview-screens'}
2. {'action': 'waitForSelector', 'target': '.ai-scores'}
**Expected Result:** Detailed AI analysis scores are displayed for the candidate.

### View comprehensive interview summary
**Steps:**
1. {'action': 'visit', 'target': '/interview-screens'}
2. {'action': 'waitForSelector', 'target': '.interview-summary'}
**Expected Result:** A comprehensive summary of the interview is displayed, including observations, positives, and negatives.

### Select or reject candidate
**Steps:**
1. {'action': 'visit', 'target': '/interview-screens'}
2. {'action': 'click', 'target': '.select-candidate-button'}
3. {'action': 'waitForSelector', 'target': '.candidate-selected'}
**Expected Result:** Candidate is successfully selected or rejected.

### Upload resumes for screening
**Steps:**
1. {'action': 'visit', 'target': '/resume-screening'}
2. {'action': 'uploadFile', 'target': '.resume-upload-input', 'file': 'example_resume.pdf'}
3. {'action': 'waitForSelector', 'target': '.resume-screening-in-progress'}
**Expected Result:** Resumes are successfully uploaded for screening.

### View resume screening results
**Steps:**
1. {'action': 'visit', 'target': '/resume-screening'}
2. {'action': 'waitForSelector', 'target': '.resume-screening-results'}
**Expected Result:** Resume screening results are displayed, including AI recommendations and scores.

### Send interview link to candidate
**Steps:**
1. {'action': 'visit', 'target': '/resume-screening'}
2. {'action': 'click', 'target': '.send-interview-link-button'}
3. {'action': 'waitForSelector', 'target': '.interview-link-sent'}
**Expected Result:** Interview link is successfully sent to the candidate.

