<!-- WVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREkwZEZsWFduQmpWMFYyWkROS2NHUkhWakZqU0UwOQ== -->

## Shadow Identity

### Objective
Identify the person in the photo.

### Solution

#### 1. Analyze the file type of the provided zip file

```bash
file shadow-identity.zip
```
The file command output the type of the file, which is a zip archive.

#### 2. Unzip the file to extract the contents.

```bash
unzip shadow-identity.zip
```
`shadow-identity.jpeg` is extracted from the zip file.

#### 3. View the image

I used image view to view the image. There's a word "MISS GRAND TANZANIA 2026" on the image, which is a hint to identify the person in the image.

#### 4. Identify the person in the image

I used Google to search for the person by using the hint "MISS GRAND TANZANIA 2026", and found the exact same image on the the search result. 

I folowed the link to the Facebook website, and found out that the person in the image is "Jihan Mohin".

![search](images/search.png)

#### 5. Find the person's real name

The challenge need the real name of the person, so I used Google to search for "Jihan Mohin real name", and found out that the real name of the person is "Jihan Mohin Dimack".

#### 6. Retrieve the flag

Construct the flag according to flag format, which is `hiCTF{<real_name>}` and lowercase.

**Flag:** hiCTF{jihan_mohin_dimack}

### Lessons Learned
- Using search engines and social media platforms can be effective in gathering information about a person.
- Understanding how to construct the flag based on the flag format is important in OSINT challenges.

---

<div align="center">
  <sub> Created by <a href="https://github.com/n-afiqa/">@n-afiqa</a> · © 2026.</sub>
</div>