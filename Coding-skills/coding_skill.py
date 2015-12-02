import json
import sys

def main():
    filename = sys.argv[1:][0]
    with open(filename, 'r') as f:
        data = json.load(f)
        people = data['people']
        skills = []
        for i in people:
            person_f_name = i['first_name']
            person_l_name = i['last_name']
            person_skills = i['skills']
            skill_dict = []           
            for j in person_skills:
                
                skill_name = j['name']
                skill_level = j['level']
                skill_values= person_f_name, skill_level
                skill_dict.append({skill_name:skill_values})
            skills.append(skill_dict)
        newskills = []
        for keys, values in skills:
            newskills.append({keys:values})
        return newskills
            
        

if __name__ == '__main__':
    print(main())

