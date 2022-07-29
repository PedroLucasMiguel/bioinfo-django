import json
from django.http import HttpResponse
from django.core import serializers
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from django.shortcuts import render

# Create your views here.

def helloWorld(request, match, mismatch, gap, seqA, seqB, algorithm):
    
    mismatch = int(mismatch)
    gap = int(gap)

    json_dict = {}

    seq1 = SeqRecord(
        Seq(seqA),
        id="seqA",
        name="seqA",
        description="seqA"
    )

    seq2 = SeqRecord(
        Seq(seqB),
        id="seqB",
        name="seqB",
        description="seqB"
    )

    if algorithm == 'nw':
        align = pairwise2.align.globalms(
            seq1.seq, 
            seq2.seq, 
            match=match, 
            mismatch=mismatch, 
            open=gap, 
            extend=gap
        )

        for r in range(len(align)):
            json_dict['Algorithm'] = 'Needleman-Wunsch'
            json_dict[f'Result-{r}'] = {'SeqA': align[r].seqA, 'SeqB': align[r].seqB, 'Score': align[r].score}

        return HttpResponse(json.dumps(json_dict, indent=4), content_type='application/json')

    elif algorithm == 'sw':
        align = pairwise2.align.localms(
            seq1.seq, 
            seq2.seq, 
            match=match, 
            mismatch=mismatch, 
            open=gap, 
            extend=gap
        )

        for r in range(len(align)):
            json_dict['Algorithm'] = "Smith Waterman"
            json_dict[f'Result-{r}'] = {'SeqA': align[r].seqA, 'SeqB': align[r].seqB, 'Score': align[r].score}

        return HttpResponse(json.dumps(json_dict, indent=4), content_type='application/json')

    return HttpResponse('Algorithms: nw or sw')