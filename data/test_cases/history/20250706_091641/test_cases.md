### Create Interview - Job Description Input
**Steps:**
1. {'action': 'fill', 'selector': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'selector': "button[type='submit']"}
**Expected Result:** AI suggests questions based on the job description

### Create Interview - Enhanced JD Feature
**Steps:**
1. {'action': 'click', 'selector': "button[role='enhanced-jd']"}
2. {'action': 'fill', 'selector': "input[name='jobTitle']", 'value': 'JavaScript developer with AWS experience'}
3. {'action': 'click', 'selector': "button[type='submit']"}
**Expected Result:** AI generates a complete job description

### Create Interview - Save Job Description
**Steps:**
1. {'action': 'click', 'selector': "button[type='save']"}
**Expected Result:** Skill recommendations are displayed

### Create Interview - Select Skills
**Steps:**
1. {'action': 'check', 'selector': "input[name='aws']"}
2. {'action': 'check', 'selector': "input[name='javascript']"}
**Expected Result:** Skills are selected and displayed

### Create Interview - Difficulty Level Selection
**Steps:**
1. {'action': 'select', 'selector': "select[name='difficultyLevel']", 'option': 'Moderate'}
**Expected Result:** Difficulty level is set to Moderate

### Create Interview - Company Name Input
**Steps:**
1. {'action': 'fill', 'selector': "input[name='companyName']", 'value': 'Test Company'}
**Expected Result:** Company name is saved

### Create Interview - Standard Questions
**Steps:**
1. {'action': 'check', 'selector': "input[name='noticePeriod']"}
**Expected Result:** Standard questions are displayed and can be personalized

### Create Interview - Role-Based Questions
**Steps:**
1. {'action': 'check', 'selector': "input[name='roleBasedQuestion']"}
**Expected Result:** Role-based questions are displayed and can be personalized

### Create Interview - Create Interview
**Steps:**
1. {'action': 'click', 'selector': "button[type='create']"}
**Expected Result:** Interview is created and unique public interview link is displayed

### View Candidate Responses and Scores
**Steps:**
1. {'action': 'click', 'element': "xpath=//a[contains(text(), 'Responses')]"}
2. {'action': 'wait', 'element': "xpath=//div[contains(text(), 'Structured answers and video recordings')]"}
**Expected Result:** The responses tab is displayed with structured answers, video recordings, scores, and resumes

### Verify Interview Scores
**Steps:**
1. {'action': 'click', 'element': "xpath=//a[contains(text(), 'Responses')]"}
2. {'action': 'get_text', 'element': "xpath=//span[contains(text(), 'Interview score')]/following-sibling::span"}
3. {'action': 'get_text', 'element': "xpath=//span[contains(text(), 'Communication score')]/following-sibling::span"}
**Expected Result:** The interview score and communication score are displayed

### Verify AI Provided Summary
**Steps:**
1. {'action': 'click', 'element': "xpath=//a[contains(text(), 'Responses')]"}
2. {'action': 'get_text', 'element': "xpath=//div[contains(text(), 'Comprehensive summary of the interview')]"}
**Expected Result:** The AI provided summary is displayed with observations, positives, and negatives

### Verify Action Buttons
**Steps:**
1. {'action': 'click', 'element': "xpath=//a[contains(text(), 'Responses')]"}
2. {'action': 'get_text', 'element': "xpath=//button[contains(text(), 'Select')]"}
3. {'action': 'get_text', 'element': "xpath=//button[contains(text(), 'Reject')]"}
**Expected Result:** The 'Select' and 'Reject' buttons are displayed

### Verify Resume Screening Process
**Steps:**
1. {'action': 'click', 'element': "xpath=//a[contains(text(), 'Resume Screening')]"}
2. {'action': 'upload_file', 'element': "xpath=//input[@type='file']", 'file_path': 'path/to/resume/files'}
3. {'action': 'click', 'element': "xpath=//button[contains(text(), 'Submit')]"}
**Expected Result:** The AI commences the resume screening process and assigns a resume score

### Verify AI Recommendations
**Steps:**
1. {'action': 'click', 'element': "xpath=//a[contains(text(), 'Resume Screening')]"}
2. {'action': 'get_text', 'element': "xpath=//div[contains(text(), 'AI recommends the profile for the next stage')]"}
**Expected Result:** The AI recommendation is displayed, indicating whether to reject the candidate or advance them to the next round

