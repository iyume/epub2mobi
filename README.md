# epub2mobi

Wide support convert ebook from EPUB to MOBI script using ebook-convert.

## Prepare

Download calibre and `ebook-convert` binary executable will be join into your $PATH.

## Usage

```txt
Usage: python3 epub2mobi.py SOURCE [TARGET]

EPUB to MOBI script, support recursively build the target.

[TARGET] is optional. If SOURCE is a file, then it should be the output file with extension (maybe not .mobi). \
If SOURCE is a folder, then it should be a folder name which will be automatically created by script. \
Wisely, you should leave it empty.

If SOURCE and [TARGET] are files, then the script run just like pure ebook-convert program. \
Ensure you have specify the extension of SOURCE and [TARGET].

Also, if TARGET is specified, the script will throw error is TARGET already exists.

Flags:
  -h, --help        display this help and exit
  -v, --detail      show convert detail from ebook-convert
  --same-dir        if given, [TARGET] will be ignore and will not separate source and target
```

## Example

```shell
Founded: collections\damaged 埃罗芒阿老师 05 和泉纱雾的初次上学.epub
Building collections-build\damaged 埃罗芒阿老师 05 和泉纱雾的初次上学.mobi
ConvertError: Please check parameter "collections\damaged 埃罗芒阿老师 05 和泉纱雾的初次上学.epub" and "collections-build\damaged 埃罗芒阿老师 05 和泉纱雾的初次上
学.mobi" is correct. Maybe source file has been damaged.

Do you want to continue? [Y/n] y

Founded: collections\埃罗芒阿老师 01 妹妹与不开之屋.ePub
Building collections-build\埃罗芒阿老师 01 妹妹与不开之屋.mobi
Founded: collections\埃罗芒阿老师 02 妹妹与世上最有趣的小说.epub
Building collections-build\埃罗芒阿老师 02 妹妹与世上最有趣的小说.mobi
Founded: collections\重启咲良田\[河野裕]重启咲良田[第1卷][简]（精排+插图）.epub
Building collections-build\重启咲良田\[河野裕]重启咲良田[第1卷][简]（精排+插图）.mobi
Founded: collections\重启咲良田\[河野裕]重启咲良田[第2卷][简]（精排+插图）.epub
Building collections-build\重启咲良田\[河野裕]重启咲良田[第2卷][简]（精排+插图）.mobi
Founded: collections\重启咲良田\more\三坪房间的侵略者！？21.epub
Building collections-build\重启咲良田\more\三坪房间的侵略者！？21.mobi
Finished.
```
