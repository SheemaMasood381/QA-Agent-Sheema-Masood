### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'selector': '#jobDescriptionInput', 'value': 'JavaScript Developer with AWS experience'}
2. {'action': 'click', 'selector': '#analyzeJobDescriptionButton'}
3. {'action': 'waitForSelector', 'selector': '#skillRecommendations'}
**Expected Result:** Skill recommendations are displayed

### Select Skills from Recommendations
**Steps:**
1. {'action': 'click', 'selector': '#selectSkillButton'}
2. {'action': 'selectOption', 'selector': '#skillSelect', 'option': 'AWS'}
3. {'action': 'click', 'selector': '#addSkillButton'}
**Expected Result:** Selected skills are added to the interview

### Configure Question Difficulty
**Steps:**
1. {'action': 'selectOption', 'selector': '#difficultySelect', 'option': 'Moderate'}
**Expected Result:** Difficulty level is updated

### Add Company Name
**Steps:**
1. {'action': 'fill', 'selector': '#companyNameInput', 'value': 'Test Company'}
2. {'action': 'click', 'selector': '#saveCompanyButton'}
**Expected Result:** Company name is saved

### Generate Standard Questions
**Steps:**
1. {'action': 'waitForSelector', 'selector': '#standardQuestions'}
**Expected Result:** Standard questions are generated

### Customize Standard Question
**Steps:**
1. {'action': 'click', 'selector': '#editStandardQuestionButton'}
2. {'action': 'fill', 'selector': '#standardQuestionInput', 'value': "What's your current job title?"}
3. {'action': 'click', 'selector': '#saveStandardQuestionButton'}
**Expected Result:** Standard question is customized

### Generate Role-Based Questions
**Steps:**
1. {'action': 'waitForSelector', 'selector': '#roleBasedQuestions'}
**Expected Result:** Role-based questions are generated

### Customize Role-Based Question
**Steps:**
1. {'action': 'click', 'selector': '#editRoleBasedQuestionButton'}
2. {'action': 'fill', 'selector': '#roleBasedQuestionInput', 'value': 'How do you handle JavaScript errors?'}
3. {'action': 'click', 'selector': '#saveRoleBasedQuestionButton'}
**Expected Result:** Role-based question is customized

### Create Interview
**Steps:**
1. {'action': 'click', 'selector': '#createInterviewButton'}
**Expected Result:** Interview is created and public link is displayed
