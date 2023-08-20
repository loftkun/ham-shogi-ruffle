#!/usr/local/bin/perl
# shogi.swf から スコアが s=123,456 のフォーマットで HTTP POSTされるので shogi_score.txt に記録する
use CGI;
my $q = new CGI;
my $score = $q->param('s');
open(DATAFILE, "> shogi_score.txt") or die("error :$!");
print DATAFILE "s=$score";
close(DATAFILE);
