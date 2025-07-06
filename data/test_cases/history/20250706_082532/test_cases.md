### Create Interview with Job Description
**Steps:**
1. {'action': 'fill', 'locator': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** AI suggests questions based on job description

### Create Interview with Enhanced JD Feature
**Steps:**
1. {'action': 'fill', 'locator': "input[name='jobTitle']", 'value': '2-year experienced JavaScript developer with AWS experience'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** AI generates a complete job description

### Select Skills from AI Recommendations
**Steps:**
1. {'action': 'wait_for_selector', 'locator': 'ul.skills-list'}
2. {'action': 'click', 'locator': "li.skill-item:has-text('AWS')"}
**Expected Result:** Selected skills are displayed

### Set Difficulty Level of Questions
**Steps:**
1. {'action': 'select_option', 'locator': "select[name='difficultyLevel']", 'option': 'Hard'}
**Expected Result:** Difficulty level is set to Hard

### Personalize Standard Questions
**Steps:**
1. {'action': 'wait_for_selector', 'locator': 'ul.questions-list'}
2. {'action': 'click', 'locator': "li.question-item:has-text('What's the notice period?') checkbox"}
**Expected Result:**  Preferred answer is selected

### Create Interview with Customized Questions
**Steps:**
1. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Interview is created with unique public interview link

### View candidate responses
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
**Expected Result:** The candidate's structured answers, video recordings, scores, and resume are displayed

### View AI analyzed scores
**Steps:**
1. Visit the interview screenings section
2. Click on a candidate's interview screening
**Expected Result:** The AI analyzed scores are displayed

### View comprehensive summary of interview
**Steps:**
1. Visit the interview screenings section
2. Click on a candidate's interview screening
**Expected Result:** A comprehensive summary of the interview, including observations, positives, and negatives is displayed

### Select or reject candidate
**Steps:**
1. Visit the interview screenings section
2. Click on a candidate's interview screening
3. Click the action button
**Expected Result:** The option to select or reject the candidate is available

### Upload resumes for screening
**Steps:**
1. Create an interview
2. Upload resumes
**Expected Result:** The AI commences the screening process

### View resume screening results
**Steps:**
1. Upload resumes for screening
2. Visit the screening results
**Expected Result:** The AI assigns a resume score and provides a recommendation for each candidate

### View AI recommendation
**Steps:**
1. View resume screening results
2. Click on a candidate's screening result
**Expected Result:** The AI recommendation is displayed, indicating suitability for the next stage

### Send interview link to candidate
**Steps:**
1. View resume screening results
2. Click on a candidate's screening result
3. Click the 'Send interview link' button
**Expected Result:** The candidate receives an interview link that is valid for 24 hours

### Review interview summary
**Steps:**
1. Send interview link to candidate
2. Wait for candidate to submit interview
3. Visit the interview screenings section
**Expected Result:** The interview summary is available for review

