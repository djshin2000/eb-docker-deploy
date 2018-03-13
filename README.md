# EB Docker Deploy Project

AWS의 Elasticbeanstalk 배포를 연습하는 프로젝트입니다.
`.secrets`폴더내의 파일로 비밀 키를 관리합니다.

### eb 배포 방법

```
git add -f .secrets && eb deploy --staged --profile=eb && git reset HEAD .secrets
```