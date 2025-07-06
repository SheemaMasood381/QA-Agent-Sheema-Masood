### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'selector': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'selector': "button[type='submit']"}
**Expected Result:** Job description is saved and skill recommendations are displayed

### Skill Selection from Suggestions
**Steps:**
1. {'action': 'click', 'selector': 'div.skill-suggestion > ul > li:first-child'}
2. {'action': 'click', 'selector': "button[type='save']"}
**Expected Result:** Selected skills are saved and displayed

### Select Question Difficulty Level
**Steps:**
1. {'action': 'select', 'selector': "select[name='difficultyLevel']", 'value': 'Moderate'}
**Expected Result:** Difficulty level is saved and displayed

### Add Standard Question
**Steps:**
1. {'action': 'click', 'selector': "button[type='add-question']"}
2. {'action': 'fill', 'selector': "input[name='question']", 'value': "What's the notice period?"}
3. {'action': 'click', 'selector': "button[type='save-question']"}
**Expected Result:** Standard question is added and displayed

### Create Interview with Customized Questions
**Steps:**
1. {'action': 'click', 'selector': "button[type='create-interview']"}
**Expected Result:** Interview is created and unique public interview link is displayed

### Verify Interview Link
**Steps:**
1. {'action': 'get', 'selector': 'a.interview-link'}
**Expected Result:** Unique public interview link is displayed

### Advance Plan - Select AI Avatar
**Steps:**
1. {'action': 'click', 'selector': "div.advance-plan > button[type='select-ai-avatar']"}
2. {'action': 'select', 'selector': "select[name='ai-avatar']", 'value': 'Default Avatar'}
**Expected Result:** AI avatar is selected and lip syncing aligns with the script

### Verify candidate's interview score and communication score
**Steps:**
1. Navigate to the responses tab
2. Click on the candidate's video interview
3. Verify the interview score and communication score are displayed
**Expected Result:** The interview score and communication score are correctly displayed

### Verify AI-generated summary of the interview
**Steps:**
1. Navigate to the responses tab
2. Click on the candidate's video interview
3. Verify the AI-generated summary is displayed, including observations, positives, and negatives
**Expected Result:** The AI-generated summary is correctly displayed

### Verify action buttons to select or reject the candidate
**Steps:**
1. Navigate to the responses tab
2. Click on the candidate's video interview
3. Verify the 'Select' and 'Reject' action buttons are displayed
**Expected Result:** The 'Select' and 'Reject' action buttons are correctly displayed

### Verify résumé screening process
**Steps:**
1. Create an interview and upload résumés
2. Verify the AI commences the screening process
3. Verify the résumé score is assigned based on skills and experience
**Expected Result:** The résumé screening process is correctly initiated and the résumé score is assigned

### Verify AI recommendations for résumé screening
**Steps:**
1. Verify the AI recommendations are displayed for each résumé
2. Verify the recommendation is based on the suitability of the résumé for the job description
**Expected Result:** The AI recommendations are correctly displayed and based on the suitability of the résumé for the job description

### Verify sending interview link to candidate
**Steps:**
1. Decide to proceed with a candidate
2. Verify the option to send an interview link is available
3. Verify the interview link is sent to the candidate and is valid for 24 hours
**Expected Result:** The interview link is correctly sent to the candidate and is valid for 24 hours

