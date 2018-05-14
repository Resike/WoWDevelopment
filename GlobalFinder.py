from SublimeLinter.lint import Linter

class GlobalFinder(Linter):
	cmd = 'luacheck - --formatter=plain --std none --only [111,112,113] --no-unused --no-redefined --no-unused-args --no-unused-secondaries --no-self --no-max-line-length --no-max-code-line-length --no-max-string-line-length --no-max-comment-line-length --codes --ranges --filename @'

	version_args = '--help'
	version_re = r'[Ll]uacheck (?P<version>\d+\.\d+\.\d+)'
	version_requirement = '>= 0.11.0, < 1.0.0'

	regex = (
		r'^.+:(?P<line>\d+):(?P<col>\d+)\-(?P<col_end>\d+): '
		r'\((?:(?P<error>E\d+)|(?P<warning>W\d+))\) '
		r'(?P<message>.+)'
	)
	defaults = {
		'selector': 'source.lua, source.lua.wow, source.luae'
	}

	def split_match(self, match):
		match, line, col, error, warning, msg, near = super().split_match(match)
		col_end = int(match.group(3))
		token_len = col_end - col
		return match, line, col, error, warning, msg, "." * token_len
