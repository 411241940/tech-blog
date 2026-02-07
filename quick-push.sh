#!/bin/bash
read -p "用户名: " u
read -s -p "Token: " t
echo ""
git push https://$u:$t@github.com/$u/tech-blog.git main
echo ""
echo "✅ 完成！"
