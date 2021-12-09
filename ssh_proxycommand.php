#! /usr/bin/php
<?php
# usage:
# $ cat > .ssh/config
# Host *..*
#   ProxyCommand /usr/local/bin/ssh_proxycommand.php %h %p
# ^D
# $ ssh user@target..jumphost..user%jumphost..jumphost


# idea:
#ssh -W where_i_want_to_go nearest_host
#ssh -W where_i_want_to_go -o ProxyCommand={{ ssh -W next_hop nearest_host }}}

function host_and_port($all)
{
	$all = str_replace('%', '@', $all);
	$all = str_replace('#', ':', $all);

	$user = null;
	$port = null;

	if (preg_match('/^(.*?)@(.*)$/i', $all, $results)) {
		$user = $results[1];
		$all = $results[2];
	}

	if (preg_match('/^(.*?):(\d+)$/i', $all, $results)) {
		$port = $results[2];
		$all = $results[1];
	}

	return array($user, $all, $port);
}

$hosts = explode('..', $argv[1]);
if (count($argv) >= 3 && is_numeric($argv[2])) {
	$hosts[0] .= ':' . $argv[2];
}

$hosts = array_reverse($hosts);

$complete_pc = '';
$first = true;

foreach ($hosts as $h) {
  $nexthop = host_and_port($h);

  if ($first) {
    $destination = $nexthop;
    $first = false;
    continue;
  }

	$new_pc = 'ssh';
  $new_pc .= ' -W '.escapeshellarg($nexthop[1].':'.($nexthop[2] === null ? 22 : $nexthop[2]));

	if ($complete_pc != '') {
		# $complete_pc = str_replace('%', '%%', $complete_pc);
		$new_pc .= ' -o ProxyCommand='.escapeshellarg($complete_pc);
	}

	if ($destination[2] !== null)
		$new_pc .= ' -p '.escapeshellarg($destination[2]);
	if ($destination[0] !== null)
		$new_pc .= ' -l '.escapeshellarg($destination[0]);
	$new_pc .= ' '.escapeshellarg($destination[1]);

  $complete_pc = $new_pc;
  $destination = $nexthop;
}

if (count($argv) > 2 && $argv[count($argv)-1] == '--dump') {
	print $complete_pc."\n";
	exit;
}

passthru($complete_pc, $return_var);
exit($return_var);

?>
