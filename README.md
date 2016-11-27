# Folder-to-Zip-Converter
Convert folder to zip file
<h2>Folder to Zip file Converter</h2>
<p>I used <b>shutil</b> Library to convert folder to zip file.</p>
<p>It provides a High-level utility to compressed and archived files.</p><br>
<h3>Syntax</h3>
<strong>shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])</strong>
<p>Create an archive file (such as zip or tar) and return its name.
<br>
<b>base_name</b> is the name of the file to create, including the path, minus any format-specific extension. format is the archive format: one of “zip”, “tar”, “bztar” (if the bz2 module is available), “xztar” (if the lzma module is available) or “gztar”.
<br>
<b>root_dir</b> is a directory that will be the root directory of the archive; for example, we typically chdir into root_dir before creating the archive.
<br>
<b>base_dir</b> is the directory where we start archiving from; i.e. base_dir will be the common prefix of all files and directories in the archive.
<br>
root_dir and base_dir both default to the current directory.
<br>
If <b>dry_run</b> is true, no archive is created, but the operations that would be executed are logged to logger.
<br>
owner and group are used when creating a tar archive. By default, uses the current owner and group.
<br>
logger must be an object compatible with PEP 282, usually an instance of logging.Logger.
<br>
The verbose argument is unused and deprecated.
<br>
Changed in version 3.5: Added support for the xztar format.
</p>
