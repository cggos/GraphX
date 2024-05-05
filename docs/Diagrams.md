# Diagrams

* xkcd styled chart
    - [xkcd](https://xkcd.com/): A webcomic of romance, sarcasm, math, and language.
    - [xkcd styled chart lib](https://github.com/timqian/chart.xkcd)

---

## Overview

* [Inkscape](https://inkscape.org/) is a professional vector graphics editor for Windows, Mac OS X and Linux. It's free and open source.
    * [InkscapeForum](http://www.inkscapeforum.com/)
    * extensions
        - [Inkscape Table Support](https://sourceforge.net/projects/inkscape-tables/)

* [Dia Diagram Editor](http://dia-installer.de/)

* [Diagram Designer](http://logicnet.dk/DiagramDesigner/): Simple vector graphics editor for creating flowcharts, UML class diagrams, illustrations and slide shows.

* [Xfig](http://mcj.sourceforge.net/) is an interactive drawing tool which runs under X Window System Version 11 Release 4 (X11R4) or later, on most UNIX-compatible platforms, and e.g. under Darwin on the MacIntosh and any X server under Microsoft Windows. It is freeware, and can be downloaded freely

* [Edraw](https://www.edrawsoft.com/): Creating flow chart, mind map, org charts, network diagrams and floor plans with rich gallery of examples and templates


### Online Tools

* [Google Diagram (draw.io)](https://app.diagrams.net/)

* [ProcessOn](https://www.processon.com/) 

* [Draw Anywhere](http://www.drawanywhere.com/): Create diagrams online. No download, no-install!

* [WebSequenceDiagrams](https://www.websequencediagrams.com/)


## Creating Graphics Programmatically

* [Mermaid](https://mermaid.js.org/)

* [GraphViz](http://www.graphviz.org/)
    * [GraphViz Pocket Reference](https://graphs.grevian.org/)
    * [GraphViz User Guide](http://graphviz.readthedocs.io/en/stable/manual.html)

* [Asymptote: The Vector Graphics Language](http://asymptote.sourceforge.net/)


## 思维导图(Mind Map)

* [15款最好用的思维导图（心智图 ）工具](http://www.cnblogs.com/lhb25/p/15-best-mind-mapping-tools-designers.html)

### MindManager

http://www.mindmanager.cn/

### XMind

[XMind](https://www.xmind.net/), a full-featured mind mapping and brainstorming tool, designed to generate ideas, inspire creativity, brings you efficiency both in work and life. Tens of million people love it.

### FreeMind

[FreeMind](http://freemind.sourceforge.net/wiki/index.php/Main_Page) is a premier free mind-mapping software written in Java

* [Free Ur Mind-推荐使用FreeMind工具](https://blog.csdn.net/qq272803220/article/details/7199728)

* 解决 Freemind 中文字体乱码
  由于 Freemind 要应用到 Java 运行时环境，显示中文字体乱码是由于 JRE 的字体造成的，所以更改 JRE 的字体即可。找一个可用于中文显示的字体，比如： wqy 字体，这里采用增黑。  
  确认字体已经安装于系统，我的系统增黑字体安装于：
  ```
  /usr/share/fonts/truetype/wqy/wqy-zenhei.ttf
  ```
  找到 JRE 的字体目录，位于：
  ```
  /usr/lib/jvm/java-6-sun/jre/lib/fonts/
  ```
  创建字体目录：
  ```sh
  cd /usr/lib/jvm/java-6-sun/jre/lib/fonts/
  sudo mkdir fallback
  sudo ln -s /usr/share/fonts/truetype/wqy/wqy-zenhei.ttf wqy-zenhei.ttf
  sudo mkfontdir
  sudo mkfontscale
  ```
  重启 Freemind 即可

### iMindMap

https://imindmap.com/zh-cn/

### Online

* [百度脑图](http://naotu.baidu.com)
* [极速灵感](http://jsmind.sinaapp.com/)
* [MyMind](http://my-mind.github.io/)
