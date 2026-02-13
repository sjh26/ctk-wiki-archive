---
title: Sandbox
---

The raw set of data retrieved using this [http://www.commontk.org/index.php/Special:GetData/Sandbox_data|URL](http://www.commontk.org/index.php/Special:GetData/Sandbox_data|URL) is reported below:

pre
Name,Color,Shape
Apple,Red,Round
Banana,Yellow,Oblong
Orange,Orange,Round
Pear,Yellow,"Pear-shaped"
/pre



*- The following table should contains Fruits*

{{#get_web_data:url=http://www.commontk.org/index.php/Special:GetData/Sandbox_data|format=CSV with header|data=name=Name,color=Color,shape=Shape}}
{| class="wikitable"
! Name
! Color `{{#for_external_table:nowiki/`
{{!}}-
{{!}} [{`{{name}}`}]({`{{name}}`}.html)
{{!}} {`{{color}}`} }}
|}




The raw set of data retrieved using this [http://discoursedb.org/wiki/Special:GetData/Fruits_data|URL](http://discoursedb.org/wiki/Special:GetData/Fruits_data|URL) is reported below:

pre
Name,Color,Shape
Apple,Red,Round
Banana,Yellow,Oblong
Orange,Orange,Round
Pear,Yellow,"Pear-shaped"
/pre

{{#get_web_data:url=http://discoursedb.org/wiki/Special:GetData/Fruits_data|format=CSV with header|data=name=Name,color=Color,shape=Shape}}
{| class="wikitable"
! Name
! Color `{{#for_external_table:nowiki/`
{{!}}-
{{!}} [{`{{name}}`}]({`{{name}}`}.html)
{{!}} {`{{color}}`} }}
|}