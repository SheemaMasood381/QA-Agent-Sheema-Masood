### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'target': 'input_job_description', 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'target': 'save_job_description_button'}
**Expected Result:** Skill recommendations are displayed

### Select Skills from AI Suggestions
**Steps:**
1. {'action': 'click', 'target': 'skill_suggestion_aws'}
2. {'action': 'click', 'target': 'skill_suggestion_javascript'}
**Expected Result:** Selected skills are displayed

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'select', 'target': 'difficulty_level_select', 'option': 'moderate'}
**Expected Result:** Difficulty level is set to moderate

### AI Suggests Standard and Role-Based Questions
**Steps:**
1. {'action': 'waitFor', 'target': 'standard_questions_list'}
2. {'action': 'waitFor', 'target': 'role_based_questions_list'}
**Expected Result:** Standard and role-based questions are displayed

### Personalize Standard Questions
**Steps:**
1. {'action': 'click', 'target': 'standard_question_edit_button'}
2. {'action': 'fill', 'target': 'standard_question_input', 'value': "What's your experience with JavaScript?"}
3. {'action': 'click', 'target': 'standard_question_save_button'}
**Expected Result:** Standard question is personalized

### Create Interview
**Steps:**
1. {'action': 'click', 'target': 'create_interview_button'}
**Expected Result:** Interview is created and unique public interview link is displayed

### View candidate responses
**Steps:**
1. Visit the responses tab
2. Verify that structured answers, video recordings, scores, and resumes are displayed for each candidate
**Expected Result:** All candidate responses are displayed with structured answers, video recordings, scores, and resumes

### View interview scores and communication scores
**Steps:**
1. Select a candidate who has completed a video interview
2. Verify that the interview score and communication score are displayed
**Expected Result:** The interview score and communication score are displayed for the selected candidate

### View AI analysis summary
**Steps:**
1. Select a candidate who has completed a video interview
2. Verify that the AI analysis summary is displayed, including observations, positives, and negatives
**Expected Result:** The AI analysis summary is displayed for the selected candidate, including observations, positives, and negatives

### Reject or select candidate
**Steps:**
1. Select a candidate who has completed a video interview
2. Verify that an action button is displayed to either select or reject the candidate
**Expected Result:** The action button to select or reject the candidate is displayed

### Upload resumes for screening
**Steps:**
1. Create an interview
2. Upload a set of resumes
3. Verify that the AI commences the screening process
**Expected Result:** The AI begins screening the uploaded resumes

### View resume scores and recommendations
**Steps:**
1. Upload a set of resumes
2. Verify that the resume scores and AI recommendations are displayed
**Expected Result:** The resume scores and AI recommendations are displayed for each uploaded resume

### Send interview link to candidate
**Steps:**
1. Select a candidate who has been recommended by the AI
2. Verify that an interview link can be sent to the candidate, valid for 24 hours
**Expected Result:** The interview link can be sent to the candidate and is valid for 24 hours

### View interview summary
**Steps:**
1. Send an interview link to a candidate
2. Wait for the candidate to submit their interview
3. Verify that the interview summary is displayed, including AI analysis
**Expected Result:** The interview summary is displayed, including AI analysis, after the candidate submits their interview

