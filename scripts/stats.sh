easy=$(leetcode list | grep ✔ | grep Easy | wc -l | xargs)
medium=$(leetcode list | grep ✔ | grep Medium | grep -v Zigzag | wc -l | xargs)
hard=$(leetcode list | grep ✔ | grep Hard | wc -l | xargs)

echo "# Progress\n## Easy\n![$easy](https://progress-bar.dev/$easy/?scale=28&suffix=/28)" > 01_easy.md
echo "## Medium\n![$medium](https://progress-bar.dev/$medium/?scale=101&suffix=/101)" > 02_medium.md
echo "## Hard\n![$hard](https://progress-bar.dev/$hard/?scale=21&suffix=/21)" > 03_hard.md


pandoc 01_easy.md 02_medium.md 03_hard.md -o README.md