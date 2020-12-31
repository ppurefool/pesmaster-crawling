import yaml

with open("../resource/pesmaster.yaml", encoding="UTF-8") as f:
    pesmasterYaml = yaml.load(f, Loader=yaml.FullLoader)
    print(pesmasterYaml)
    print(pesmasterYaml["cheat-engine"])
    print(pesmasterYaml["cheat-engine"]["title"])
