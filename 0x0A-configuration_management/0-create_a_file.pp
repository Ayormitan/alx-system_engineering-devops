# Puppet manifest that creates a file school in tmpdirectory
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
