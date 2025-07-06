### Create Interview - Enter Job Description
**Steps:**
1. {'action': 'fill', 'locator': "input[name='jobDescription']", 'value': 'JavaScript developer with AWS experience'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Job description is saved and skill recommendations are displayed

### Create Interview - Prefill and Edit Job Description
**Steps:**
1. {'action': 'click', 'locator': "button[aria-label='Enhanced JD feature']"}
2. {'action': 'fill', 'locator': "input[name='jobTitle']", 'value': 'JavaScript developer with AWS experience'}
3. {'action': 'click', 'locator': "button[type='submit']"}
4. {'action': 'fill', 'locator': "input[name='jobDescription']", 'value': ' Edited job description'}
5. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Job description is prefilled, edited and saved

### Create Interview - Choose Skills
**Steps:**
1. {'action': 'select', 'locator': "select[name='skills']", 'value': 'AWS'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Selected skills are saved

### Create Interview - Configure Question Difficulty
**Steps:**
1. {'action': 'select', 'locator': "select[name='difficultyLevel']", 'value': 'Moderate'}
2. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Question difficulty level is configured

### Create Interview - Review and Save Questions
**Steps:**
1. {'action': 'click', 'locator': "button[aria-label='Review questions']"}
2. {'action': 'check', 'locator': "input[name='standardQuestionPreferredAnswer']"}
3. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Questions are reviewed and saved with preferred answers

### Create Interview - Create Interview
**Steps:**
1. {'action': 'click', 'locator': "button[type='submit']"}
**Expected Result:** Interview is created with a unique public link

### Create Interview - Verify Interview Link
**Steps:**
1. {'action': 'get', 'locator': 'a[href*=public-interview-link]'}
**Expected Result:** Public interview link is displayed and valid

### View candidate responses
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
**Expected Result:** Fully view structured answers, video recordings, scores, and resumes

### View interview scores
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Check the interview score
**Expected Result:** Display the candidate's interview score

### View communication scores
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Check the communication score
**Expected Result:** Display the candidate's communication score

### View AI analysis summary
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Check the AI analysis summary
**Expected Result:** Display a comprehensive summary of the interview, including observations, positives, and negatives

### Take action on a candidate
**Steps:**
1. Visit the responses tab
2. Click on a candidate's response
3. Click the action button
**Expected Result:** Allow user to select or reject the candidate

### Screen resumes against a job description
**Steps:**
1. Create an interview
2. Upload multiple resumes
3. Submit for screening
**Expected Result:** AI commences the screening process and assigns a resume score to each candidate

### View AI recommendations
**Steps:**
1. Create an interview
2. Upload multiple resumes
3. Submit for screening
4. View AI recommendations
**Expected Result:** Display a list of candidates with their resume scores and AI recommendations

### Reject or advance a candidate
**Steps:**
1. Create an interview
2. Upload multiple resumes
3. Submit for screening
4. View AI recommendations
5. Click on a candidate's profile
**Expected Result:** Allow user to reject or advance the candidate to the next round

### Send interview link to candidate
**Steps:**
1. Create an interview
2. Upload multiple resumes
3. Submit for screening
4. View AI recommendations
5. Click on a candidate's profile
6. Click 'Send interview link'
**Expected Result:** Send an interview link to the candidate, valid for 24 hours

