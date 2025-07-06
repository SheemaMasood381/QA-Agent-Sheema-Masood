### Create Interview with Job Description
**Steps:**
1. {'step': 'Visit the create interview page', 'expected_result': 'The page should be loaded successfully'}
2. {'step': 'Enter a job description', 'input': 'JavaScript developer with AWS experience', 'expected_result': 'The AI should suggest questions based on the job description'}
3. {'step': 'Verify the suggested questions', 'expected_result': 'The questions should be relevant to the job description'}
**Expected Result:** 

### Use Enhanced JD Feature
**Steps:**
1. {'step': 'Enter a job title', 'input': '2-year experienced JavaScript developer with AWS experience', 'expected_result': 'The AI should generate a complete job description'}
2. {'step': 'Verify the generated job description', 'expected_result': 'The job description should be accurate and relevant to the job title'}
**Expected Result:** 

### Select Skills from AI Suggestions
**Steps:**
1. {'step': 'Save the job description', 'expected_result': 'Skill recommendations should be displayed'}
2. {'step': 'Select skills from AI suggestions', 'input': ['AWS', 'JavaScript'], 'expected_result': 'The selected skills should be displayed'}
**Expected Result:** 

### Customize Standard Questions
**Steps:**
1. {'step': 'Click on a standard question', 'expected_result': 'The question should be editable'}
2. {'step': 'Edit a standard question', 'input': "What's the notice period?", 'expected_result': 'The edited question should be saved successfully'}
**Expected Result:** 

### Create Role-Based Questions
**Steps:**
1. {'step': 'Click on the role-based questions tab', 'expected_result': 'The role-based questions should be displayed'}
2. {'step': 'Edit a role-based question', 'input': "What's your experience with AWS?", 'expected_result': 'The edited question should be saved successfully'}
**Expected Result:** 

### Create Interview
**Steps:**
1. {'step': 'Click on the create option', 'expected_result': 'The interview should be created successfully'}
2. {'step': 'Verify the unique public interview link', 'expected_result': 'The link should be displayed and functional'}
**Expected Result:** 

### Test candidate video interview submission
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview response
**Expected Result:** The candidate's video interview response is displayed with scores and resume

### Test interview score display
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview response
**Expected Result:** The candidate's interview score is displayed

### Test communication score display
**Steps:**
1. Visit the responses tab
2. Click on a candidate's video interview response
**Expected Result:** The candidate's communication score is displayed

### Test AI analysis scoring
**Steps:**
1. Visit the interview screenings section
2. Select a candidate's video interview response
**Expected Result:** The AI analysis scores are displayed for the selected candidate

### Test candidate ré screening
**Steps:**
1. Create an interview and upload multiple résumés
2. Submit the résumés for screening
**Expected Result:** The AI conducts a comprehensive semantic analysis and assigns a ré score for each candidate

### Test ré score display
**Steps:**
1. Visit the ré screening results
2. Select a candidate's résumé
**Expected Result:** The candidate's ré score is displayed along with the AI recommendation

### Test AI recommendation logic
**Steps:**
1. Visit the ré screening results
2. Select a candidate's résumé with a high score but not recommended by the AI
**Expected Result:** The AI recommendation logic is correctly applied, considering the candidate's overall experience in relation to the job description

### Test interview link sending
**Steps:**
1. Visit the ré screening results
2. Select a candidate's résumé and decide to proceed
3. Send an interview link to the candidate
**Expected Result:** The interview link is sent to the candidate and is valid for 24 hours

### Test interview submission and review
**Steps:**
1. Wait for the candidate to submit their interview
2. Visit the responses tab
3. Click on the candidate's interview response
**Expected Result:** The candidate's interview response is displayed with scores and resume, and the AI analysis summary is available

