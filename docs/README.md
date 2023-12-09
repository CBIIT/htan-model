<link rel='stylesheet' href="assets/style.css">
<link rel='stylesheet' href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossorigin="">
<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script type="text/javascript"  src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"></script>
<script type="text/javascript" src="assets/actions.js"></script>

![Build Status](https://github.com/CBIIT/htan-model/actions/workflows/model-test-and-deploy.yml/badge.svg)

# Human Tumor Atlas Network Data Model Representation

This is a representation of the [JSONLD-based HTAN data model](https://github.com/ncihtan/data-models.git) in [Model Description Format](https://github.com/CBIIT/bento-mdf).

[View model on GitHub Pages](https://cbiit.github.io/icdc-model-tool/)


Zoom to Node: <select id="node_select">
  <option value="">Zoom to Node</option>
</select>
<div id="model"></div>

<p>
<a href="./model-desc/htan-model.svg">SVG file (in view above)</a>
<p>
<a href="./model-desc">Additional model files</a>
<div id='graph' style='display:off;'>
<svg width="6820pt" height="653pt"
 viewBox="0.00 0.00 6819.59 653.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 649)">
<title>Perl</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-649 6815.5894,-649 6815.5894,4 -4,4"/>
<!-- Exposure -->
<g id="node1" class="node">
<title>Exposure</title>
<ellipse fill="none" stroke="#000000" cx="1207.5894" cy="-18" rx="54.6905" ry="18"/>
<text text-anchor="middle" x="1207.5894" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Exposure</text>
</g>
<!-- SRRSClinicalDataTier2 -->
<g id="node2" class="node">
<title>SRRSClinicalDataTier2</title>
<ellipse fill="none" stroke="#000000" cx="119.5894" cy="-192" rx="119.6788" ry="18"/>
<text text-anchor="middle" x="119.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSClinicalDataTier2</text>
</g>
<!-- Patient -->
<g id="node61" class="node">
<title>Patient</title>
<ellipse fill="none" stroke="#000000" cx="1721.5894" cy="-105" rx="44.393" ry="18"/>
<text text-anchor="middle" x="1721.5894" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">Patient</text>
</g>
<!-- SRRSClinicalDataTier2&#45;&gt;Patient -->
<g id="edge24" class="edge">
<title>SRRSClinicalDataTier2&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M179.2577,-176.2689C227.9357,-164.2018 298.6913,-148.3982 361.5894,-141 620.9318,-110.4955 1446.8732,-105.8292 1667.1573,-105.124"/>
<polygon fill="#000000" stroke="#000000" points="1667.1953,-108.624 1677.1845,-105.0933 1667.1738,-101.624 1667.1953,-108.624"/>
<text text-anchor="middle" x="435.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MolecularTest -->
<g id="node3" class="node">
<title>MolecularTest</title>
<ellipse fill="none" stroke="#000000" cx="1377.5894" cy="-18" rx="77.1866" ry="18"/>
<text text-anchor="middle" x="1377.5894" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">MolecularTest</text>
</g>
<!-- ScRNA_seqLevel1 -->
<g id="node4" class="node">
<title>ScRNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="849.5894" cy="-279" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="849.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel1</text>
</g>
<!-- Biospecimen -->
<g id="node72" class="node">
<title>Biospecimen</title>
<ellipse fill="none" stroke="#000000" cx="2800.5894" cy="-192" rx="70.3881" ry="18"/>
<text text-anchor="middle" x="2800.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">Biospecimen</text>
</g>
<!-- ScRNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge20" class="edge">
<title>ScRNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M855.0138,-261.0065C859.5595,-249.3636 867.3185,-235.0981 879.5894,-228 923.8821,-202.379 2670.7695,-215.9679 2721.5894,-210 2727.9155,-209.2571 2734.4754,-208.2139 2740.9883,-206.9998"/>
<polygon fill="#000000" stroke="#000000" points="2742.024,-210.3621 2751.144,-204.9698 2740.6519,-203.4978 2742.024,-210.3621"/>
<text text-anchor="middle" x="953.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- PancreaticCancerTier3 -->
<g id="node5" class="node">
<title>PancreaticCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="376.5894" cy="-192" rx="118.8789" ry="18"/>
<text text-anchor="middle" x="376.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">PancreaticCancerTier3</text>
</g>
<!-- PancreaticCancerTier3&#45;&gt;Patient -->
<g id="edge21" class="edge">
<title>PancreaticCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M430.5538,-175.9358C473.4864,-163.9374 535.3189,-148.3883 590.5894,-141 802.4528,-112.6793 1471.3336,-106.4937 1667.1989,-105.2753"/>
<polygon fill="#000000" stroke="#000000" points="1667.2743,-108.775 1677.2529,-105.2146 1667.2319,-101.7751 1667.2743,-108.775"/>
<text text-anchor="middle" x="664.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel3 -->
<g id="node6" class="node">
<title>MassSpectrometryLevel3</title>
<ellipse fill="none" stroke="#000000" cx="2446.5894" cy="-453" rx="130.777" ry="18"/>
<text text-anchor="middle" x="2446.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel3</text>
</g>
<!-- MassSpectrometryLevel2 -->
<g id="node63" class="node">
<title>MassSpectrometryLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2446.5894" cy="-366" rx="130.777" ry="18"/>
<text text-anchor="middle" x="2446.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel2</text>
</g>
<!-- MassSpectrometryLevel3&#45;&gt;MassSpectrometryLevel2 -->
<g id="edge23" class="edge">
<title>MassSpectrometryLevel3&#45;&gt;MassSpectrometryLevel2</title>
<path fill="none" stroke="#000000" d="M2446.5894,-434.9735C2446.5894,-423.1918 2446.5894,-407.5607 2446.5894,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="2450.0895,-394.0033 2446.5894,-384.0034 2443.0895,-394.0034 2450.0895,-394.0033"/>
<text text-anchor="middle" x="2520.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- OtherAssay -->
<g id="node7" class="node">
<title>OtherAssay</title>
<ellipse fill="none" stroke="#000000" cx="1029.5894" cy="-279" rx="65.7887" ry="18"/>
<text text-anchor="middle" x="1029.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">OtherAssay</text>
</g>
<!-- OtherAssay&#45;&gt;Biospecimen -->
<g id="edge22" class="edge">
<title>OtherAssay&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1029.0397,-260.9483C1029.7598,-249.5912 1032.818,-235.6774 1042.5894,-228 1079.2646,-199.184 2675.2687,-215.4619 2721.5894,-210 2727.9152,-209.2541 2734.4748,-208.2089 2740.9876,-206.9937"/>
<polygon fill="#000000" stroke="#000000" points="2742.0238,-210.3558 2751.1432,-204.9625 2740.6509,-203.4917 2742.0238,-210.3558"/>
<text text-anchor="middle" x="1116.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3 -->
<g id="node8" class="node">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3</title>
<ellipse fill="none" stroke="#000000" cx="3810.5894" cy="-453" rx="258.0542" ry="18"/>
<text text-anchor="middle" x="3810.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPSpatialTranscriptomicsLevel3</text>
</g>
<!-- NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="node14" class="node">
<title>NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<ellipse fill="none" stroke="#000000" cx="3462.5894" cy="-279" rx="294.3478" ry="18"/>
<text text-anchor="middle" x="3462.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="edge17" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M3658.593,-438.444C3541.3499,-425.6389 3396.1027,-405.697 3377.5894,-384 3354.112,-356.4852 3389.768,-324.016 3421.8315,-302.5469"/>
<polygon fill="#000000" stroke="#000000" points="3423.8045,-305.4392 3430.2965,-297.0663 3420.0001,-299.5632 3423.8045,-305.4392"/>
<text text-anchor="middle" x="3451.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel2 -->
<g id="node40" class="node">
<title>ImagingLevel2</title>
<ellipse fill="none" stroke="#000000" cx="4374.5894" cy="-366" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="4374.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel2</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;ImagingLevel2 -->
<g id="edge16" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M3958.4551,-438.2454C3992.9738,-433.0518 4029.3516,-426.1396 4062.5894,-417 4079.3024,-412.4043 4081.8446,-406.4783 4098.5894,-402 4159.1938,-385.7916 4176.3821,-392.1157 4238.5894,-384 4256.8224,-381.6213 4276.427,-379.0403 4294.9176,-376.5953"/>
<polygon fill="#000000" stroke="#000000" points="4295.6055,-380.0348 4305.0599,-375.2531 4294.6871,-373.0953 4295.6055,-380.0348"/>
<text text-anchor="middle" x="4172.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1 -->
<g id="node47" class="node">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</title>
<ellipse fill="none" stroke="#000000" cx="3792.5894" cy="-366" rx="258.0542" ry="18"/>
<text text-anchor="middle" x="3792.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPSpatialTranscriptomicsLevel1 -->
<g id="edge18" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</title>
<path fill="none" stroke="#000000" d="M3806.8598,-434.9735C3804.4222,-423.1918 3801.1881,-407.5607 3798.4152,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="3801.7678,-393.0868 3796.3142,-384.0034 3794.9129,-394.5051 3801.7678,-393.0868"/>
<text text-anchor="middle" x="3876.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="node77" class="node">
<title>NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<ellipse fill="none" stroke="#000000" cx="4253.5894" cy="-279" rx="295.1477" ry="18"/>
<text text-anchor="middle" x="4253.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="edge15" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M3883.3302,-435.709C3906.2112,-430.0308 3931.5227,-423.5019 3954.5894,-417 4001.6719,-403.7287 4014.5394,-403.0628 4059.5894,-384 4115.9141,-360.1663 4177.4609,-325.2078 4215.7958,-302.279"/>
<polygon fill="#000000" stroke="#000000" points="4217.7902,-305.1638 4224.5534,-297.0084 4214.1806,-299.1662 4217.7902,-305.1638"/>
<text text-anchor="middle" x="4205.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel1 -->
<g id="node9" class="node">
<title>BulkWESLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1200.5894" cy="-279" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="1200.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel1</text>
</g>
<!-- BulkWESLevel1&#45;&gt;Biospecimen -->
<g id="edge19" class="edge">
<title>BulkWESLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1195.3149,-260.9866C1193.2866,-249.94 1193.1657,-236.3585 1201.5894,-228 1216.5761,-213.1292 2700.6234,-212.4841 2721.5894,-210 2727.9148,-209.2506 2734.4741,-208.2031 2740.9868,-206.9864"/>
<polygon fill="#000000" stroke="#000000" points="2742.0235,-210.3484 2751.1421,-204.9539 2740.6497,-203.4846 2742.0235,-210.3484"/>
<text text-anchor="middle" x="1275.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SRRSBiospecimen -->
<g id="node10" class="node">
<title>SRRSBiospecimen</title>
<ellipse fill="none" stroke="#000000" cx="610.5894" cy="-192" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="610.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSBiospecimen</text>
</g>
<!-- SRRSBiospecimen&#45;&gt;Patient -->
<g id="edge27" class="edge">
<title>SRRSBiospecimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M660.8203,-176.526C702.1879,-164.5216 762.6037,-148.6752 816.5894,-141 982.2254,-117.4512 1497.8009,-108.1774 1667.1112,-105.7178"/>
<polygon fill="#000000" stroke="#000000" points="1667.3352,-109.2151 1677.2841,-105.5723 1667.235,-102.2158 1667.3352,-109.2151"/>
<text text-anchor="middle" x="890.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel3 -->
<g id="node11" class="node">
<title>ElectronMicroscopyLevel3</title>
<ellipse fill="none" stroke="#000000" cx="4980.5894" cy="-453" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="4980.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel3</text>
</g>
<!-- ElectronMicroscopyLevel2 -->
<g id="node71" class="node">
<title>ElectronMicroscopyLevel2</title>
<ellipse fill="none" stroke="#000000" cx="4875.5894" cy="-366" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="4875.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel2</text>
</g>
<!-- ElectronMicroscopyLevel3&#45;&gt;ElectronMicroscopyLevel2 -->
<g id="edge26" class="edge">
<title>ElectronMicroscopyLevel3&#45;&gt;ElectronMicroscopyLevel2</title>
<path fill="none" stroke="#000000" d="M4959.8919,-435.145C4948.3875,-425.287 4933.7734,-412.8728 4920.5894,-402 4915.9413,-398.1668 4910.99,-394.1449 4906.1353,-390.2353"/>
<polygon fill="#000000" stroke="#000000" points="4908.1184,-387.3392 4898.1269,-383.8148 4903.7397,-392.8007 4908.1184,-387.3392"/>
<text text-anchor="middle" x="5010.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel1 -->
<g id="node12" class="node">
<title>BulkMethylation_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1531.5894" cy="-279" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="1531.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel1</text>
</g>
<!-- BulkMethylation_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge25" class="edge">
<title>BulkMethylation_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1531.4268,-260.9284C1532.3835,-249.5628 1535.7177,-235.6471 1545.5894,-228 1571.4169,-207.9925 2689.1525,-213.9002 2721.5894,-210 2727.9135,-209.2396 2734.472,-208.185 2740.9841,-206.9642"/>
<polygon fill="#000000" stroke="#000000" points="2742.0227,-210.3257 2751.1389,-204.9272 2740.6459,-203.4624 2742.0227,-210.3257"/>
<text text-anchor="middle" x="1619.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel2 -->
<g id="node13" class="node">
<title>BulkMethylation_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1534.5894" cy="-366" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="1534.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel2</text>
</g>
<!-- BulkMethylation_seqLevel2&#45;&gt;BulkMethylation_seqLevel1 -->
<g id="edge30" class="edge">
<title>BulkMethylation_seqLevel2&#45;&gt;BulkMethylation_seqLevel1</title>
<path fill="none" stroke="#000000" d="M1533.9678,-347.9735C1533.5615,-336.1918 1533.0225,-320.5607 1532.5604,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1536.0528,-306.8768 1532.2102,-297.0034 1529.057,-307.1181 1536.0528,-306.8768"/>
<text text-anchor="middle" x="1606.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel2&#45;&gt;Biospecimen -->
<g id="edge29" class="edge">
<title>BulkMethylation_seqLevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1621.4591,-351.8116C1648.5691,-345.9784 1674.1247,-338.5676 1684.5894,-330 1710.7455,-308.5856 1688.9495,-280.4616 1716.5894,-261 1849.4092,-167.4796 1918.4331,-237.6179 2080.5894,-228 2365.0906,-211.1256 2438.8493,-245.829 2721.5894,-210 2727.9085,-209.1992 2734.4637,-208.1186 2740.974,-206.8821"/>
<polygon fill="#000000" stroke="#000000" points="2742.0191,-210.2417 2751.1268,-204.8287 2740.6314,-203.3806 2742.0191,-210.2417"/>
<text text-anchor="middle" x="1790.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScDNA_seqLevel1 -->
<g id="node15" class="node">
<title>ScDNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1970.5894" cy="-279" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="1970.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScDNA_seqLevel1</text>
</g>
<!-- ScDNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge28" class="edge">
<title>ScDNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2015.4047,-262.991C2051.416,-250.938 2103.5677,-235.2897 2150.5894,-228 2401.496,-189.1021 2469.7552,-242.3527 2721.5894,-210 2727.9071,-209.1884 2734.4615,-208.1007 2740.9711,-206.8601"/>
<polygon fill="#000000" stroke="#000000" points="2742.018,-210.2191 2751.1234,-204.8022 2740.6274,-203.3586 2742.018,-210.2191"/>
<text text-anchor="middle" x="2224.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Demographics -->
<g id="node16" class="node">
<title>Demographics</title>
<ellipse fill="none" stroke="#000000" cx="1550.5894" cy="-18" rx="77.9862" ry="18"/>
<text text-anchor="middle" x="1550.5894" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Demographics</text>
</g>
<!-- ElectronMicroscopyLevel4 -->
<g id="node17" class="node">
<title>ElectronMicroscopyLevel4</title>
<ellipse fill="none" stroke="#000000" cx="4980.5894" cy="-540" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="4980.5894" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel4</text>
</g>
<!-- ElectronMicroscopyLevel4&#45;&gt;ElectronMicroscopyLevel3 -->
<g id="edge34" class="edge">
<title>ElectronMicroscopyLevel4&#45;&gt;ElectronMicroscopyLevel3</title>
<path fill="none" stroke="#000000" d="M4980.5894,-521.9735C4980.5894,-510.1918 4980.5894,-494.5607 4980.5894,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="4984.0895,-481.0033 4980.5894,-471.0034 4977.0895,-481.0034 4984.0895,-481.0033"/>
<text text-anchor="middle" x="5054.5894" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Image -->
<g id="node18" class="node">
<title>ImagingLevel3Image</title>
<ellipse fill="none" stroke="#000000" cx="4533.5894" cy="-453" rx="109.6807" ry="18"/>
<text text-anchor="middle" x="4533.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Image</text>
</g>
<!-- ImagingLevel3Image&#45;&gt;ImagingLevel2 -->
<g id="edge31" class="edge">
<title>ImagingLevel3Image&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M4470.4166,-438.1477C4454.4397,-432.857 4437.7975,-425.9244 4423.5894,-417 4412.9741,-410.3323 4403.0324,-400.8715 4394.9154,-391.9059"/>
<polygon fill="#000000" stroke="#000000" points="4397.4706,-389.5099 4388.281,-384.2372 4392.1768,-394.0898 4397.4706,-389.5099"/>
<text text-anchor="middle" x="4497.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Channels -->
<g id="node69" class="node">
<title>ImagingLevel3Channels</title>
<ellipse fill="none" stroke="#000000" cx="4597.5894" cy="-366" rx="124.2781" ry="18"/>
<text text-anchor="middle" x="4597.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Channels</text>
</g>
<!-- ImagingLevel3Image&#45;&gt;ImagingLevel3Channels -->
<g id="edge32" class="edge">
<title>ImagingLevel3Image&#45;&gt;ImagingLevel3Channels</title>
<path fill="none" stroke="#000000" d="M4558.0756,-435.2569C4564.3454,-429.8956 4570.6921,-423.6506 4575.5894,-417 4580.7925,-409.934 4585.0764,-401.4472 4588.4371,-393.4426"/>
<polygon fill="#000000" stroke="#000000" points="4591.7287,-394.6348 4592.0784,-384.0458 4585.2016,-392.1056 4591.7287,-394.6348"/>
<text text-anchor="middle" x="4657.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- LungCancerTier3 -->
<g id="node19" class="node">
<title>LungCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="818.5894" cy="-192" rx="92.8835" ry="18"/>
<text text-anchor="middle" x="818.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">LungCancerTier3</text>
</g>
<!-- LungCancerTier3&#45;&gt;Patient -->
<g id="edge33" class="edge">
<title>LungCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M873.2226,-177.4148C920.1596,-165.5185 989.8323,-149.362 1051.5894,-141 1169.9987,-124.9672 1528.9135,-111.5114 1666.8123,-106.7988"/>
<polygon fill="#000000" stroke="#000000" points="1667.2564,-110.2859 1677.1318,-106.4484 1667.0187,-103.2899 1667.2564,-110.2859"/>
<text text-anchor="middle" x="1125.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ProstateCancerTier3 -->
<g id="node20" class="node">
<title>ProstateCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="1037.5894" cy="-192" rx="108.5808" ry="18"/>
<text text-anchor="middle" x="1037.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">ProstateCancerTier3</text>
</g>
<!-- ProstateCancerTier3&#45;&gt;Patient -->
<g id="edge2" class="edge">
<title>ProstateCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1099.3945,-177.1978C1149.5612,-165.7023 1222.2697,-150.2148 1286.5894,-141 1422.9088,-121.47 1584.8944,-111.5266 1667.4126,-107.4007"/>
<polygon fill="#000000" stroke="#000000" points="1667.7398,-110.889 1677.5562,-106.903 1667.3966,-103.8974 1667.7398,-110.889"/>
<text text-anchor="middle" x="1360.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- AcuteLymphoblasticLeukemiaTier3 -->
<g id="node21" class="node">
<title>AcuteLymphoblasticLeukemiaTier3</title>
<ellipse fill="none" stroke="#000000" cx="1341.5894" cy="-192" rx="177.3685" ry="18"/>
<text text-anchor="middle" x="1341.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">AcuteLymphoblasticLeukemiaTier3</text>
</g>
<!-- AcuteLymphoblasticLeukemiaTier3&#45;&gt;Patient -->
<g id="edge1" class="edge">
<title>AcuteLymphoblasticLeukemiaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1385.036,-174.4669C1413.7418,-163.4723 1452.4198,-149.7692 1487.5894,-141 1548.7104,-125.7601 1620.5128,-115.8652 1668.303,-110.3774"/>
<polygon fill="#000000" stroke="#000000" points="1668.8748,-113.8353 1678.4213,-109.2402 1668.093,-106.8791 1668.8748,-113.8353"/>
<text text-anchor="middle" x="1561.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- FollowUp -->
<g id="node22" class="node">
<title>FollowUp</title>
<ellipse fill="none" stroke="#000000" cx="1721.5894" cy="-18" rx="54.6905" ry="18"/>
<text text-anchor="middle" x="1721.5894" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">FollowUp</text>
</g>
<!-- MelanomaTier3 -->
<g id="node23" class="node">
<title>MelanomaTier3</title>
<ellipse fill="none" stroke="#000000" cx="1620.5894" cy="-192" rx="83.6854" ry="18"/>
<text text-anchor="middle" x="1620.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">MelanomaTier3</text>
</g>
<!-- MelanomaTier3&#45;&gt;Patient -->
<g id="edge6" class="edge">
<title>MelanomaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1628.9595,-173.7977C1634.5107,-163.2268 1642.6067,-150.2193 1652.5894,-141 1660.6381,-133.5668 1670.5105,-127.2307 1680.2439,-122.0425"/>
<polygon fill="#000000" stroke="#000000" points="1682.0957,-125.0295 1689.4692,-117.4215 1678.9606,-118.7707 1682.0957,-125.0295"/>
<text text-anchor="middle" x="1726.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel4 -->
<g id="node24" class="node">
<title>ImagingLevel4</title>
<ellipse fill="none" stroke="#000000" cx="4746.5894" cy="-453" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="4746.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel4</text>
</g>
<!-- ImagingLevel4&#45;&gt;ImagingLevel3Channels -->
<g id="edge4" class="edge">
<title>ImagingLevel4&#45;&gt;ImagingLevel3Channels</title>
<path fill="none" stroke="#000000" d="M4747.1692,-434.7714C4746.5272,-423.9227 4743.8611,-410.6331 4735.5894,-402 4728.0877,-394.1706 4709.5656,-387.4846 4688.4421,-382.0761"/>
<polygon fill="#000000" stroke="#000000" points="4689.1275,-378.6409 4678.5839,-379.6815 4687.4752,-385.4431 4689.1275,-378.6409"/>
<text text-anchor="middle" x="4817.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel4 -->
<g id="node25" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="5474.5894" cy="-627" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="5474.5894" y="-623.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel4</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3 -->
<g id="node35" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="5474.5894" cy="-540" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="5474.5894" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel4&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel3 -->
<g id="edge5" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel4&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</title>
<path fill="none" stroke="#000000" d="M5474.5894,-608.9735C5474.5894,-597.1918 5474.5894,-581.5607 5474.5894,-568.1581"/>
<polygon fill="#000000" stroke="#000000" points="5478.0895,-568.0033 5474.5894,-558.0034 5471.0895,-568.0034 5478.0895,-568.0033"/>
<text text-anchor="middle" x="5548.5894" y="-579.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SRRSImagingLevel2 -->
<g id="node26" class="node">
<title>SRRSImagingLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2191.5894" cy="-279" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="2191.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSImagingLevel2</text>
</g>
<!-- SRRSImagingLevel2&#45;&gt;Biospecimen -->
<g id="edge3" class="edge">
<title>SRRSImagingLevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2236.966,-262.609C2271.9001,-250.7694 2321.6543,-235.5802 2366.5894,-228 2522.3689,-201.7214 2565.0966,-231.6292 2721.5894,-210 2727.8076,-209.1406 2734.2584,-208.0338 2740.6718,-206.7921"/>
<polygon fill="#000000" stroke="#000000" points="2741.5843,-210.178 2750.6805,-204.7458 2740.182,-203.3199 2741.5843,-210.178"/>
<text text-anchor="middle" x="2440.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Diagnosis -->
<g id="node27" class="node">
<title>Diagnosis</title>
<ellipse fill="none" stroke="#000000" cx="1892.5894" cy="-18" rx="55.7903" ry="18"/>
<text text-anchor="middle" x="1892.5894" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Diagnosis</text>
</g>
<!-- MassSpectrometryLevel1 -->
<g id="node28" class="node">
<title>MassSpectrometryLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2446.5894" cy="-279" rx="130.777" ry="18"/>
<text text-anchor="middle" x="2446.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel1</text>
</g>
<!-- MassSpectrometryLevel1&#45;&gt;Biospecimen -->
<g id="edge9" class="edge">
<title>MassSpectrometryLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2478.5226,-261.4956C2500.8489,-250.071 2531.7206,-235.8655 2560.5894,-228 2630.0585,-209.0726 2650.5979,-222.0168 2721.5894,-210 2727.4536,-209.0074 2733.5357,-207.8516 2739.6037,-206.6137"/>
<polygon fill="#000000" stroke="#000000" points="2740.7014,-209.9591 2749.7616,-204.4671 2739.254,-203.1104 2740.7014,-209.9591"/>
<text text-anchor="middle" x="2634.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel1 -->
<g id="node29" class="node">
<title>ScATAC_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2695.5894" cy="-279" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="2695.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel1</text>
</g>
<!-- ScATAC_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge8" class="edge">
<title>ScATAC_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2703.0926,-260.6652C2708.1749,-250.0474 2715.7575,-237.037 2725.5894,-228 2732.6923,-221.4713 2741.1948,-215.8987 2749.8828,-211.2276"/>
<polygon fill="#000000" stroke="#000000" points="2751.5796,-214.2923 2758.9529,-206.6841 2748.4443,-208.0337 2751.5796,-214.2923"/>
<text text-anchor="middle" x="2799.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel2 -->
<g id="node30" class="node">
<title>ScRNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="849.5894" cy="-366" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="849.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel2</text>
</g>
<!-- ScRNA_seqLevel2&#45;&gt;ScRNA_seqLevel1 -->
<g id="edge7" class="edge">
<title>ScRNA_seqLevel2&#45;&gt;ScRNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M849.5894,-347.9735C849.5894,-336.1918 849.5894,-320.5607 849.5894,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="853.0895,-307.0033 849.5894,-297.0034 846.0895,-307.0034 853.0895,-307.0033"/>
<text text-anchor="middle" x="923.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScmC_seqLevel2 -->
<g id="node31" class="node">
<title>ScmC_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2905.5894" cy="-366" rx="90.9839" ry="18"/>
<text text-anchor="middle" x="2905.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScmC_seqLevel2</text>
</g>
<!-- ScmC_seqLevel1 -->
<g id="node41" class="node">
<title>ScmC_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2905.5894" cy="-279" rx="90.9839" ry="18"/>
<text text-anchor="middle" x="2905.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScmC_seqLevel1</text>
</g>
<!-- ScmC_seqLevel2&#45;&gt;ScmC_seqLevel1 -->
<g id="edge14" class="edge">
<title>ScmC_seqLevel2&#45;&gt;ScmC_seqLevel1</title>
<path fill="none" stroke="#000000" d="M2905.5894,-347.9735C2905.5894,-336.1918 2905.5894,-320.5607 2905.5894,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="2909.0895,-307.0033 2905.5894,-297.0034 2902.0895,-307.0034 2909.0895,-307.0033"/>
<text text-anchor="middle" x="2979.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Segmentation -->
<g id="node32" class="node">
<title>ImagingLevel3Segmentation</title>
<ellipse fill="none" stroke="#000000" cx="4255.5894" cy="-453" rx="145.6742" ry="18"/>
<text text-anchor="middle" x="4255.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Segmentation</text>
</g>
<!-- ImagingLevel3Segmentation&#45;&gt;ImagingLevel2 -->
<g id="edge13" class="edge">
<title>ImagingLevel3Segmentation&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M4251.0333,-434.7727C4249.4989,-424.1929 4249.6483,-411.1849 4256.5894,-402 4263.0284,-393.4795 4282.3577,-386.1343 4303.5572,-380.3417"/>
<polygon fill="#000000" stroke="#000000" points="4304.5889,-383.69 4313.3895,-377.7908 4302.831,-376.9143 4304.5889,-383.69"/>
<text text-anchor="middle" x="4330.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel2 -->
<g id="node33" class="node">
<title>BulkRNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="6663.5894" cy="-366" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="6663.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel2</text>
</g>
<!-- BulkRNA_seqLevel1 -->
<g id="node68" class="node">
<title>BulkRNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="6504.5894" cy="-279" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="6504.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel1</text>
</g>
<!-- BulkRNA_seqLevel2&#45;&gt;BulkRNA_seqLevel1 -->
<g id="edge10" class="edge">
<title>BulkRNA_seqLevel2&#45;&gt;BulkRNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M6631.7955,-348.6033C6606.7992,-334.9261 6571.818,-315.7854 6544.864,-301.037"/>
<polygon fill="#000000" stroke="#000000" points="6546.5095,-297.9478 6536.0568,-296.218 6543.1494,-304.0886 6546.5095,-297.9478"/>
<text text-anchor="middle" x="6667.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- FamilyHistory -->
<g id="node34" class="node">
<title>FamilyHistory</title>
<ellipse fill="none" stroke="#000000" cx="2063.5894" cy="-18" rx="77.1866" ry="18"/>
<text text-anchor="middle" x="2063.5894" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">FamilyHistory</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles -->
<g id="node36" class="node">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</title>
<ellipse fill="none" stroke="#000000" cx="5561.5894" cy="-453" rx="243.1569" ry="18"/>
<text text-anchor="middle" x="5561.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_AuxiliaryFiles -->
<g id="edge11" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</title>
<path fill="none" stroke="#000000" d="M5492.6158,-521.9735C5505.2142,-509.3752 5522.2139,-492.3755 5536.1839,-478.4055"/>
<polygon fill="#000000" stroke="#000000" points="5538.9898,-480.5493 5543.586,-471.0034 5534.04,-475.5996 5538.9898,-480.5493"/>
<text text-anchor="middle" x="5596.5894" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="node45" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="5282.5894" cy="-366" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="5282.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="edge12" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M5327.9924,-525.3335C5257.3108,-514.9222 5183.1997,-497.8931 5161.5894,-471 5135.2139,-438.1768 5182.3503,-407.4542 5225.2768,-387.8268"/>
<polygon fill="#000000" stroke="#000000" points="5226.899,-390.9364 5234.6274,-383.6891 5224.0664,-384.5352 5226.899,-390.9364"/>
<text text-anchor="middle" x="5235.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="edge65" class="edge">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M5479.7249,-435.9753C5456.8367,-430.5778 5432.0782,-424.1347 5409.5894,-417 5383.5137,-408.7274 5355.204,-397.5799 5331.9443,-387.8168"/>
<polygon fill="#000000" stroke="#000000" points="5333.2099,-384.5519 5322.6369,-383.8714 5330.4779,-390.9967 5333.2099,-384.5519"/>
<text text-anchor="middle" x="5483.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="node54" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5288.5894" cy="-279" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="5288.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="edge64" class="edge">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M5564.2442,-434.7923C5566.5334,-411.5133 5566.5842,-371.4239 5544.5894,-348 5524.4841,-326.5884 5460.8062,-309.3774 5401.9943,-297.4998"/>
<polygon fill="#000000" stroke="#000000" points="5402.3347,-293.9994 5391.8455,-295.4922 5400.9762,-300.8663 5402.3347,-293.9994"/>
<text text-anchor="middle" x="5635.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel3 -->
<g id="node37" class="node">
<title>BulkWESLevel3</title>
<ellipse fill="none" stroke="#000000" cx="1192.5894" cy="-453" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="1192.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel3</text>
</g>
<!-- BulkWESLevel2 -->
<g id="node59" class="node">
<title>BulkWESLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1192.5894" cy="-366" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="1192.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel2</text>
</g>
<!-- BulkWESLevel3&#45;&gt;BulkWESLevel2 -->
<g id="edge67" class="edge">
<title>BulkWESLevel3&#45;&gt;BulkWESLevel2</title>
<path fill="none" stroke="#000000" d="M1192.5894,-434.9735C1192.5894,-423.1918 1192.5894,-407.5607 1192.5894,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="1196.0895,-394.0033 1192.5894,-384.0034 1189.0895,-394.0034 1196.0895,-394.0033"/>
<text text-anchor="middle" x="1266.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BreastCancerTier3 -->
<g id="node38" class="node">
<title>BreastCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="1822.5894" cy="-192" rx="100.1823" ry="18"/>
<text text-anchor="middle" x="1822.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">BreastCancerTier3</text>
</g>
<!-- BreastCancerTier3&#45;&gt;Patient -->
<g id="edge68" class="edge">
<title>BreastCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1818.2233,-173.6047C1814.8991,-162.9653 1809.3629,-149.9537 1800.5894,-141 1791.4334,-131.656 1779.4046,-124.5097 1767.5036,-119.1451"/>
<polygon fill="#000000" stroke="#000000" points="1768.6217,-115.8197 1758.044,-115.2168 1765.937,-122.2844 1768.6217,-115.8197"/>
<text text-anchor="middle" x="1884.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HTANRPPAAntibodyTable -->
<g id="node39" class="node">
<title>HTANRPPAAntibodyTable</title>
<ellipse fill="none" stroke="#000000" cx="6406.5894" cy="-366" rx="132.6765" ry="18"/>
<text text-anchor="middle" x="6406.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">HTANRPPAAntibodyTable</text>
</g>
<!-- RPPALevel2 -->
<g id="node67" class="node">
<title>RPPALevel2</title>
<ellipse fill="none" stroke="#000000" cx="6188.5894" cy="-279" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="6188.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel2</text>
</g>
<!-- HTANRPPAAntibodyTable&#45;&gt;RPPALevel2 -->
<g id="edge66" class="edge">
<title>HTANRPPAAntibodyTable&#45;&gt;RPPALevel2</title>
<path fill="none" stroke="#000000" d="M6387.8399,-347.9853C6375.3641,-336.9382 6358.1019,-323.3565 6340.5894,-315 6315.1973,-302.8835 6285.4223,-294.6752 6258.9871,-289.1973"/>
<polygon fill="#000000" stroke="#000000" points="6259.5242,-285.7359 6249.0352,-287.2292 6258.1661,-292.6029 6259.5242,-285.7359"/>
<text text-anchor="middle" x="6437.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel1 -->
<g id="node53" class="node">
<title>ImagingLevel1</title>
<ellipse fill="none" stroke="#000000" cx="4647.5894" cy="-279" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="4647.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel1</text>
</g>
<!-- ImagingLevel2&#45;&gt;ImagingLevel1 -->
<g id="edge74" class="edge">
<title>ImagingLevel2&#45;&gt;ImagingLevel1</title>
<path fill="none" stroke="#000000" d="M4420.9001,-351.2416C4467.9639,-336.2433 4540.9191,-312.9938 4591.2923,-296.9408"/>
<polygon fill="#000000" stroke="#000000" points="4592.5863,-300.2019 4601.0515,-293.8308 4590.4608,-293.5324 4592.5863,-300.2019"/>
<text text-anchor="middle" x="4600.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScmC_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge73" class="edge">
<title>ScmC_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2897.2949,-260.7148C2891.7706,-250.1145 2883.6763,-237.1052 2873.5894,-228 2866.5049,-221.605 2858.0775,-216.0786 2849.5089,-211.4076"/>
<polygon fill="#000000" stroke="#000000" points="2851.0767,-208.2783 2840.5787,-206.849 2847.8941,-214.5129 2851.0767,-208.2783"/>
<text text-anchor="middle" x="2959.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel3 -->
<g id="node42" class="node">
<title>RPPALevel3</title>
<ellipse fill="none" stroke="#000000" cx="3082.5894" cy="-279" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="3082.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel3</text>
</g>
<!-- RPPALevel3&#45;&gt;Biospecimen -->
<g id="edge69" class="edge">
<title>RPPALevel3&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M3071.5825,-260.7817C3063.6392,-249.3542 3051.829,-235.4246 3037.5894,-228 2974.9202,-195.3239 2949.2622,-221.8687 2879.5894,-210 2873.7262,-209.0012 2867.6448,-207.8413 2861.5772,-206.6008"/>
<polygon fill="#000000" stroke="#000000" points="2861.9278,-203.0976 2851.4198,-204.4513 2860.4785,-209.9459 2861.9278,-203.0976"/>
<text text-anchor="middle" x="3129.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel3 -->
<g id="node43" class="node">
<title>ScATAC_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="2695.5894" cy="-453" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="2695.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel3</text>
</g>
<!-- ScATAC_seqLevel2 -->
<g id="node57" class="node">
<title>ScATAC_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2695.5894" cy="-366" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="2695.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel2</text>
</g>
<!-- ScATAC_seqLevel3&#45;&gt;ScATAC_seqLevel2 -->
<g id="edge72" class="edge">
<title>ScATAC_seqLevel3&#45;&gt;ScATAC_seqLevel2</title>
<path fill="none" stroke="#000000" d="M2695.5894,-434.9735C2695.5894,-423.1918 2695.5894,-407.5607 2695.5894,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="2699.0895,-394.0033 2695.5894,-384.0034 2692.0895,-394.0034 2699.0895,-394.0033"/>
<text text-anchor="middle" x="2769.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel3 -->
<g id="node44" class="node">
<title>BulkMethylation_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="1485.5894" cy="-453" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="1485.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel3</text>
</g>
<!-- BulkMethylation_seqLevel3&#45;&gt;BulkMethylation_seqLevel2 -->
<g id="edge71" class="edge">
<title>BulkMethylation_seqLevel3&#45;&gt;BulkMethylation_seqLevel2</title>
<path fill="none" stroke="#000000" d="M1495.7422,-434.9735C1502.575,-422.8418 1511.7066,-406.6287 1519.3995,-392.9698"/>
<polygon fill="#000000" stroke="#000000" points="1522.5917,-394.4341 1524.4496,-384.0034 1516.4926,-390.9989 1522.5917,-394.4341"/>
<text text-anchor="middle" x="1586.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel3&#45;&gt;Biospecimen -->
<g id="edge70" class="edge">
<title>BulkMethylation_seqLevel3&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1445.3119,-435.7067C1423.8383,-424.2808 1399.1217,-407.1186 1385.5894,-384 1357.9656,-336.8073 1347.6042,-303.0269 1382.5894,-261 1425.7063,-209.2047 1463.659,-235.8836 1530.5894,-228 1793.469,-197.0358 2458.7824,-241.5739 2721.5894,-210 2727.9135,-209.2402 2734.4721,-208.186 2740.9842,-206.9654"/>
<polygon fill="#000000" stroke="#000000" points="2742.0227,-210.3269 2751.1391,-204.9287 2740.6461,-203.4636 2742.0227,-210.3269"/>
<text text-anchor="middle" x="1435.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel2&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="edge84" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel2&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M5283.8326,-347.9735C5284.6451,-336.1918 5285.7231,-320.5607 5286.6475,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="5290.1514,-307.2205 5287.3478,-297.0034 5283.168,-306.7388 5290.1514,-307.2205"/>
<text text-anchor="middle" x="5359.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel4 -->
<g id="node46" class="node">
<title>RPPALevel4</title>
<ellipse fill="none" stroke="#000000" cx="6188.5894" cy="-366" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="6188.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel4</text>
</g>
<!-- RPPALevel4&#45;&gt;RPPALevel2 -->
<g id="edge80" class="edge">
<title>RPPALevel4&#45;&gt;RPPALevel2</title>
<path fill="none" stroke="#000000" d="M6188.5894,-347.9735C6188.5894,-336.1918 6188.5894,-320.5607 6188.5894,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="6192.0895,-307.0033 6188.5894,-297.0034 6185.0895,-307.0034 6192.0895,-307.0033"/>
<text text-anchor="middle" x="6262.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="edge83" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M3709.8837,-348.892C3684.36,-343.2718 3656.2271,-336.7296 3630.5894,-330 3596.1384,-320.9569 3558.1347,-309.5433 3526.9997,-299.8075"/>
<polygon fill="#000000" stroke="#000000" points="3527.7348,-296.3698 3517.1455,-296.7106 3525.6361,-303.0478 3527.7348,-296.3698"/>
<text text-anchor="middle" x="3704.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;Biospecimen -->
<g id="edge82" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M3793.8179,-347.8179C3794.3313,-323.7935 3791.1577,-282.0633 3765.5894,-261 3669.7158,-182.0188 3331.6047,-235.0699 3207.5894,-228 3061.8289,-219.6904 3024.1698,-230.2895 2879.5894,-210 2873.373,-209.1276 2866.9233,-208.0124 2860.5106,-206.7656"/>
<polygon fill="#000000" stroke="#000000" points="2861.0019,-203.2936 2850.5027,-204.7139 2859.5961,-210.151 2861.0019,-203.2936"/>
<text text-anchor="middle" x="3860.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="edge81" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M3831.0106,-348.098C3856.9009,-336.8041 3892.1259,-322.9045 3924.5894,-315 3962.9318,-305.664 4004.3807,-298.7463 4044.5096,-293.6212"/>
<polygon fill="#000000" stroke="#000000" points="4045.1891,-297.0637 4054.6807,-292.3564 4044.3253,-290.1172 4045.1891,-297.0637"/>
<text text-anchor="middle" x="3998.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel2 -->
<g id="node48" class="node">
<title>HI_C_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="6015.5894" cy="-366" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="6015.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel2</text>
</g>
<!-- HI_C_seqLevel1 -->
<g id="node66" class="node">
<title>HI_C_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="6015.5894" cy="-279" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="6015.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel1</text>
</g>
<!-- HI_C_seqLevel2&#45;&gt;HI_C_seqLevel1 -->
<g id="edge78" class="edge">
<title>HI_C_seqLevel2&#45;&gt;HI_C_seqLevel1</title>
<path fill="none" stroke="#000000" d="M6015.5894,-347.9735C6015.5894,-336.1918 6015.5894,-320.5607 6015.5894,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="6019.0895,-307.0033 6015.5894,-297.0034 6012.0895,-307.0034 6019.0895,-307.0033"/>
<text text-anchor="middle" x="6089.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ColorectalCancerTier3 -->
<g id="node49" class="node">
<title>ColorectalCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="2058.5894" cy="-192" rx="117.7793" ry="18"/>
<text text-anchor="middle" x="2058.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">ColorectalCancerTier3</text>
</g>
<!-- ColorectalCancerTier3&#45;&gt;Patient -->
<g id="edge79" class="edge">
<title>ColorectalCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2031.5621,-174.4304C2012.913,-163.1288 1987.146,-149.0917 1962.5894,-141 1900.5083,-120.5435 1825.575,-111.6662 1775.9181,-107.8426"/>
<polygon fill="#000000" stroke="#000000" points="1775.9468,-104.3356 1765.7193,-107.1011 1775.4391,-111.3171 1775.9468,-104.3356"/>
<text text-anchor="middle" x="2069.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel1 -->
<g id="node50" class="node">
<title>ElectronMicroscopyLevel1</title>
<ellipse fill="none" stroke="#000000" cx="4881.5894" cy="-279" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="4881.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel1</text>
</g>
<!-- ElectronMicroscopyLevel1&#45;&gt;Biospecimen -->
<g id="edge77" class="edge">
<title>ElectronMicroscopyLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M4800.5515,-264.4909C4727.6011,-252.1619 4617.313,-235.3318 4520.5894,-228 4156.944,-200.4351 3241.7636,-252.751 2879.5894,-210 2873.2637,-209.2533 2866.7041,-208.2076 2860.1914,-206.9921"/>
<polygon fill="#000000" stroke="#000000" points="2860.5281,-203.4902 2850.0358,-204.9606 2859.1551,-210.3542 2860.5281,-203.4902"/>
<text text-anchor="middle" x="4723.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel4 -->
<g id="node51" class="node">
<title>ScATAC_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="2695.5894" cy="-540" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="2695.5894" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel4</text>
</g>
<!-- ScATAC_seqLevel4&#45;&gt;ScATAC_seqLevel3 -->
<g id="edge75" class="edge">
<title>ScATAC_seqLevel4&#45;&gt;ScATAC_seqLevel3</title>
<path fill="none" stroke="#000000" d="M2695.5894,-521.9735C2695.5894,-510.1918 2695.5894,-494.5607 2695.5894,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="2699.0895,-481.0033 2695.5894,-471.0034 2692.0895,-481.0034 2699.0895,-481.0033"/>
<text text-anchor="middle" x="2769.5894" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ClinicalDataTier2 -->
<g id="node52" class="node">
<title>ClinicalDataTier2</title>
<ellipse fill="none" stroke="#000000" cx="2287.5894" cy="-192" rx="92.8835" ry="18"/>
<text text-anchor="middle" x="2287.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">ClinicalDataTier2</text>
</g>
<!-- ClinicalDataTier2&#45;&gt;Patient -->
<g id="edge76" class="edge">
<title>ClinicalDataTier2&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2250.3689,-175.3681C2222.6133,-163.7296 2183.4619,-148.9023 2147.5894,-141 2078.1079,-125.694 1873.7791,-113.123 1775.5417,-107.7746"/>
<polygon fill="#000000" stroke="#000000" points="1775.6953,-104.2779 1765.5213,-107.2342 1775.3182,-111.2678 1775.6953,-104.2779"/>
<text text-anchor="middle" x="2272.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel1&#45;&gt;Biospecimen -->
<g id="edge42" class="edge">
<title>ImagingLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M4590.6696,-266.2454C4579.7383,-264.1855 4568.346,-262.3042 4557.5894,-261 4225.9184,-220.7871 4140.5218,-238.5772 3806.5894,-228 3600.6538,-221.4771 3084.1038,-235.017 2879.5894,-210 2873.2669,-209.2266 2866.7094,-208.1637 2860.1979,-206.9378"/>
<polygon fill="#000000" stroke="#000000" points="2860.5375,-203.4361 2850.0437,-204.8955 2859.1572,-210.2986 2860.5375,-203.4361"/>
<text text-anchor="middle" x="4442.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge40" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5167.7654,-263.1217C5069.3776,-250.9703 4926.778,-235.1251 4801.5894,-228 4588.3695,-215.8646 3091.7018,-234.8653 2879.5894,-210 2873.2631,-209.2584 2866.7032,-208.216 2860.1901,-207.0024"/>
<polygon fill="#000000" stroke="#000000" points="2860.5264,-203.5004 2850.0344,-204.973 2859.1547,-210.3647 2860.5264,-203.5004"/>
<text text-anchor="middle" x="5049.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel2 -->
<g id="node55" class="node">
<title>Slide_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="5823.5894" cy="-366" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="5823.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel2</text>
</g>
<!-- Slide_seqLevel1 -->
<g id="node65" class="node">
<title>Slide_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5700.5894" cy="-279" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="5700.5894" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel1</text>
</g>
<!-- Slide_seqLevel2&#45;&gt;Slide_seqLevel1 -->
<g id="edge41" class="edge">
<title>Slide_seqLevel2&#45;&gt;Slide_seqLevel1</title>
<path fill="none" stroke="#000000" d="M5798.9941,-348.6033C5780.1393,-335.267 5753.9406,-316.7362 5733.3158,-302.1479"/>
<polygon fill="#000000" stroke="#000000" points="5735.3273,-299.2837 5725.142,-296.3665 5731.2851,-304.9986 5735.3273,-299.2837"/>
<text text-anchor="middle" x="5842.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel4 -->
<g id="node56" class="node">
<title>ScRNA_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="849.5894" cy="-540" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="849.5894" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel4</text>
</g>
<!-- ScRNA_seqLevel3 -->
<g id="node62" class="node">
<title>ScRNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="849.5894" cy="-453" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="849.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel3</text>
</g>
<!-- ScRNA_seqLevel4&#45;&gt;ScRNA_seqLevel3 -->
<g id="edge37" class="edge">
<title>ScRNA_seqLevel4&#45;&gt;ScRNA_seqLevel3</title>
<path fill="none" stroke="#000000" d="M849.5894,-521.9735C849.5894,-510.1918 849.5894,-494.5607 849.5894,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="853.0895,-481.0033 849.5894,-471.0034 846.0895,-481.0034 853.0895,-481.0033"/>
<text text-anchor="middle" x="923.5894" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel2&#45;&gt;ScATAC_seqLevel1 -->
<g id="edge38" class="edge">
<title>ScATAC_seqLevel2&#45;&gt;ScATAC_seqLevel1</title>
<path fill="none" stroke="#000000" d="M2695.5894,-347.9735C2695.5894,-336.1918 2695.5894,-320.5607 2695.5894,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="2699.0895,-307.0033 2695.5894,-297.0034 2692.0895,-307.0034 2699.0895,-307.0033"/>
<text text-anchor="middle" x="2769.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NeuroblastomaandGliomaTier3 -->
<g id="node58" class="node">
<title>NeuroblastomaandGliomaTier3</title>
<ellipse fill="none" stroke="#000000" cx="2555.5894" cy="-192" rx="157.0724" ry="18"/>
<text text-anchor="middle" x="2555.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">NeuroblastomaandGliomaTier3</text>
</g>
<!-- NeuroblastomaandGliomaTier3&#45;&gt;Patient -->
<g id="edge39" class="edge">
<title>NeuroblastomaandGliomaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2499.6031,-175.0652C2458.7129,-163.4373 2401.7168,-148.7533 2350.5894,-141 2240.559,-124.3142 1908.0269,-111.4088 1776.2383,-106.8165"/>
<polygon fill="#000000" stroke="#000000" points="1776.0964,-103.3096 1765.9814,-106.4618 1775.8544,-110.3054 1776.0964,-103.3096"/>
<text text-anchor="middle" x="2498.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel2&#45;&gt;BulkWESLevel1 -->
<g id="edge35" class="edge">
<title>BulkWESLevel2&#45;&gt;BulkWESLevel1</title>
<path fill="none" stroke="#000000" d="M1192.1865,-347.5393C1192.1675,-337.83 1192.4482,-325.7437 1193.5894,-315 1193.8601,-312.4516 1194.2187,-309.8146 1194.6309,-307.1799"/>
<polygon fill="#000000" stroke="#000000" points="1198.0966,-307.6822 1196.4136,-297.2219 1191.2061,-306.4486 1198.0966,-307.6822"/>
<text text-anchor="middle" x="1267.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel3 -->
<g id="node60" class="node">
<title>HI_C_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="6101.5894" cy="-453" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="6101.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel3</text>
</g>
<!-- HI_C_seqLevel3&#45;&gt;HI_C_seqLevel2 -->
<g id="edge36" class="edge">
<title>HI_C_seqLevel3&#45;&gt;HI_C_seqLevel2</title>
<path fill="none" stroke="#000000" d="M6089.232,-435.1345C6081.7795,-424.9293 6071.7795,-412.1793 6061.5894,-402 6057.4528,-397.8678 6052.8462,-393.7708 6048.1911,-389.9028"/>
<polygon fill="#000000" stroke="#000000" points="6050.3767,-387.1691 6040.3856,-383.6436 6045.9975,-392.6301 6050.3767,-387.1691"/>
<text text-anchor="middle" x="6148.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Exposure -->
<g id="edge46" class="edge">
<title>Patient&#45;&gt;Exposure</title>
<path fill="none" stroke="#000000" d="M1677.4393,-103.9591C1565.4499,-101.0024 1276.5553,-91.2839 1239.5894,-69 1230.487,-63.5129 1223.5671,-54.339 1218.5319,-45.2726"/>
<polygon fill="#000000" stroke="#000000" points="1221.5266,-43.4328 1213.9545,-36.0224 1215.2528,-46.5374 1221.5266,-43.4328"/>
<text text-anchor="middle" x="1313.5894" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;MolecularTest -->
<g id="edge48" class="edge">
<title>Patient&#45;&gt;MolecularTest</title>
<path fill="none" stroke="#000000" d="M1677.7738,-102.192C1596.5343,-96.6664 1428.7494,-83.6385 1406.5894,-69 1398.0111,-63.3333 1391.689,-54.2067 1387.1775,-45.2294"/>
<polygon fill="#000000" stroke="#000000" points="1390.3713,-43.7975 1383.1129,-36.0796 1383.9741,-46.6394 1390.3713,-43.7975"/>
<text text-anchor="middle" x="1480.5894" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Demographics -->
<g id="edge47" class="edge">
<title>Patient&#45;&gt;Demographics</title>
<path fill="none" stroke="#000000" d="M1679.2497,-99.5023C1640.1275,-93.636 1585.6992,-83.2256 1569.5894,-69 1562.768,-62.9764 1558.39,-54.2666 1555.5824,-45.7444"/>
<polygon fill="#000000" stroke="#000000" points="1558.9375,-44.7429 1552.9556,-35.9983 1552.1787,-46.5647 1558.9375,-44.7429"/>
<text text-anchor="middle" x="1643.5894" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;FollowUp -->
<g id="edge45" class="edge">
<title>Patient&#45;&gt;FollowUp</title>
<path fill="none" stroke="#000000" d="M1721.5894,-86.9735C1721.5894,-75.1918 1721.5894,-59.5607 1721.5894,-46.1581"/>
<polygon fill="#000000" stroke="#000000" points="1725.0895,-46.0033 1721.5894,-36.0034 1718.0895,-46.0034 1725.0895,-46.0033"/>
<text text-anchor="middle" x="1795.5894" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Diagnosis -->
<g id="edge51" class="edge">
<title>Patient&#45;&gt;Diagnosis</title>
<path fill="none" stroke="#000000" d="M1763.6733,-99.1109C1801.8593,-93.0197 1854.5645,-82.5059 1870.5894,-69 1877.6909,-63.0148 1882.5628,-54.3145 1885.8777,-45.7892"/>
<polygon fill="#000000" stroke="#000000" points="1889.2865,-46.6278 1889.0941,-36.0347 1882.6385,-44.4357 1889.2865,-46.6278"/>
<text text-anchor="middle" x="1955.5894" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;FamilyHistory -->
<g id="edge49" class="edge">
<title>Patient&#45;&gt;FamilyHistory</title>
<path fill="none" stroke="#000000" d="M1765.2823,-102.1179C1845.834,-96.4908 2011.5681,-83.3326 2033.5894,-69 2042.2796,-63.3439 2048.7808,-54.2195 2053.4682,-45.2411"/>
<polygon fill="#000000" stroke="#000000" points="2056.6805,-46.6335 2057.7121,-36.089 2050.33,-43.6887 2056.6805,-46.6335"/>
<text text-anchor="middle" x="2121.5894" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Therapy -->
<g id="node73" class="node">
<title>Therapy</title>
<ellipse fill="none" stroke="#000000" cx="2234.5894" cy="-18" rx="49.2915" ry="18"/>
<text text-anchor="middle" x="2234.5894" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Therapy</text>
</g>
<!-- Patient&#45;&gt;Therapy -->
<g id="edge50" class="edge">
<title>Patient&#45;&gt;Therapy</title>
<path fill="none" stroke="#000000" d="M1765.7272,-103.8398C1876.955,-100.6122 2162.5339,-90.3277 2199.5894,-69 2209.2223,-63.4557 2216.787,-54.0582 2222.3814,-44.8295"/>
<polygon fill="#000000" stroke="#000000" points="2225.5895,-46.2581 2227.3225,-35.8059 2219.4497,-42.896 2225.5895,-46.2581"/>
<text text-anchor="middle" x="2289.5894" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel3&#45;&gt;ScRNA_seqLevel2 -->
<g id="edge53" class="edge">
<title>ScRNA_seqLevel3&#45;&gt;ScRNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M849.5894,-434.9735C849.5894,-423.1918 849.5894,-407.5607 849.5894,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="853.0895,-394.0033 849.5894,-384.0034 846.0895,-394.0034 853.0895,-394.0033"/>
<text text-anchor="middle" x="923.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel2&#45;&gt;MassSpectrometryLevel1 -->
<g id="edge52" class="edge">
<title>MassSpectrometryLevel2&#45;&gt;MassSpectrometryLevel1</title>
<path fill="none" stroke="#000000" d="M2446.5894,-347.9735C2446.5894,-336.1918 2446.5894,-320.5607 2446.5894,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="2450.0895,-307.0033 2446.5894,-297.0034 2443.0895,-307.0034 2450.0895,-307.0033"/>
<text text-anchor="middle" x="2520.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel3 -->
<g id="node64" class="node">
<title>Slide_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="5909.5894" cy="-453" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="5909.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel3</text>
</g>
<!-- Slide_seqLevel3&#45;&gt;Slide_seqLevel2 -->
<g id="edge44" class="edge">
<title>Slide_seqLevel3&#45;&gt;Slide_seqLevel2</title>
<path fill="none" stroke="#000000" d="M5891.7701,-434.9735C5879.2336,-422.2912 5862.288,-405.1486 5848.4271,-391.1265"/>
<polygon fill="#000000" stroke="#000000" points="5850.6108,-388.357 5841.0916,-383.7057 5845.6325,-393.2781 5850.6108,-388.357"/>
<text text-anchor="middle" x="5945.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge43" class="edge">
<title>Slide_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5626.6502,-269.5084C5602.4346,-266.5653 5575.3853,-263.4539 5550.5894,-261 5362.9348,-242.429 5315.9869,-236.0932 5127.5894,-228 4878.0338,-217.2796 3127.6961,-238.914 2879.5894,-210 2873.0181,-209.2342 2866.1949,-208.1422 2859.4342,-206.8698"/>
<polygon fill="#000000" stroke="#000000" points="2860.1042,-203.4346 2849.6103,-204.8934 2858.7235,-210.2971 2860.1042,-203.4346"/>
<text text-anchor="middle" x="5433.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge58" class="edge">
<title>HI_C_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5941.8854,-269.3485C5843.8503,-257.0144 5665.0538,-236.271 5511.5894,-228 5219.5619,-212.2612 3170.0945,-243.6831 2879.5894,-210 2873.0176,-209.238 2866.1942,-208.1485 2859.4333,-206.8775"/>
<polygon fill="#000000" stroke="#000000" points="2860.103,-203.4422 2849.6093,-204.9025 2858.7232,-210.3049 2860.103,-203.4422"/>
<text text-anchor="middle" x="5765.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel2&#45;&gt;Biospecimen -->
<g id="edge57" class="edge">
<title>RPPALevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M6139.046,-266.5952C6129.949,-264.5524 6120.5101,-262.5872 6111.5894,-261 5993.4343,-239.9775 5963.3521,-235.7108 5843.5894,-228 5514.9305,-206.8396 3206.7516,-247.8064 2879.5894,-210 2873.0173,-209.2405 2866.1937,-208.1526 2859.4327,-206.8825"/>
<polygon fill="#000000" stroke="#000000" points="2860.1021,-203.4471 2849.6086,-204.9084 2858.723,-210.31 2860.1021,-203.4471"/>
<text text-anchor="middle" x="6074.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge56" class="edge">
<title>BulkRNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M6432.7767,-265.62C6361.8668,-253.1133 6250.189,-235.3035 6152.5894,-228 5789.9312,-200.8617 3240.8694,-251.644 2879.5894,-210 2873.0171,-209.2424 2866.1933,-208.1557 2859.4323,-206.8863"/>
<polygon fill="#000000" stroke="#000000" points="2860.1015,-203.4509 2849.6081,-204.9128 2858.7229,-210.3138 2860.1015,-203.4509"/>
<text text-anchor="middle" x="6361.5894" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel4 -->
<g id="node70" class="node">
<title>MassSpectrometryLevel4</title>
<ellipse fill="none" stroke="#000000" cx="2446.5894" cy="-540" rx="130.777" ry="18"/>
<text text-anchor="middle" x="2446.5894" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel4</text>
</g>
<!-- MassSpectrometryLevel4&#45;&gt;MassSpectrometryLevel3 -->
<g id="edge54" class="edge">
<title>MassSpectrometryLevel4&#45;&gt;MassSpectrometryLevel3</title>
<path fill="none" stroke="#000000" d="M2446.5894,-521.9735C2446.5894,-510.1918 2446.5894,-494.5607 2446.5894,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="2450.0895,-481.0033 2446.5894,-471.0034 2443.0895,-481.0034 2450.0895,-481.0033"/>
<text text-anchor="middle" x="2520.5894" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel2&#45;&gt;ElectronMicroscopyLevel1 -->
<g id="edge55" class="edge">
<title>ElectronMicroscopyLevel2&#45;&gt;ElectronMicroscopyLevel1</title>
<path fill="none" stroke="#000000" d="M4876.8326,-347.9735C4877.6451,-336.1918 4878.7231,-320.5607 4879.6475,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="4883.1514,-307.2205 4880.3478,-297.0034 4876.168,-306.7388 4883.1514,-307.2205"/>
<text text-anchor="middle" x="4952.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Biospecimen&#45;&gt;Patient -->
<g id="edge63" class="edge">
<title>Biospecimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2753.4159,-178.625C2708.3958,-166.4906 2638.4574,-149.2727 2576.5894,-141 2420.8771,-120.1788 1938.9451,-109.1905 1776.0383,-105.9984"/>
<polygon fill="#000000" stroke="#000000" points="1775.8421,-102.4941 1765.7761,-105.7994 1775.7064,-109.4927 1775.8421,-102.4941"/>
<text text-anchor="middle" x="2730.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScDNA_seqLevel2 -->
<g id="node74" class="node">
<title>ScDNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1970.5894" cy="-366" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="1970.5894" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScDNA_seqLevel2</text>
</g>
<!-- ScDNA_seqLevel2&#45;&gt;ScDNA_seqLevel1 -->
<g id="edge61" class="edge">
<title>ScDNA_seqLevel2&#45;&gt;ScDNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M1970.5894,-347.9735C1970.5894,-336.1918 1970.5894,-320.5607 1970.5894,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1974.0895,-307.0033 1970.5894,-297.0034 1967.0895,-307.0034 1974.0895,-307.0033"/>
<text text-anchor="middle" x="2044.5894" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- OvarianCancerTier3 -->
<g id="node75" class="node">
<title>OvarianCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="2995.5894" cy="-192" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="2995.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">OvarianCancerTier3</text>
</g>
<!-- OvarianCancerTier3&#45;&gt;Patient -->
<g id="edge60" class="edge">
<title>OvarianCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2948.2057,-175.7779C2910.792,-163.7777 2857.0042,-148.3013 2808.5894,-141 2706.2788,-125.5708 1982.2972,-110.1715 1776.2055,-106.0619"/>
<polygon fill="#000000" stroke="#000000" points="1775.9988,-102.5572 1765.9312,-105.8579 1775.8597,-109.5558 1775.9988,-102.5572"/>
<text text-anchor="middle" x="2949.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SarcomaTier3 -->
<g id="node76" class="node">
<title>SarcomaTier3</title>
<ellipse fill="none" stroke="#000000" cx="3196.5894" cy="-192" rx="76.8869" ry="18"/>
<text text-anchor="middle" x="3196.5894" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">SarcomaTier3</text>
</g>
<!-- SarcomaTier3&#45;&gt;Patient -->
<g id="edge62" class="edge">
<title>SarcomaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M3156.3232,-176.5395C3122.5228,-164.3705 3072.6681,-148.2896 3027.5894,-141 2902.9932,-120.8517 2007.7962,-108.5253 1776.1831,-105.6503"/>
<polygon fill="#000000" stroke="#000000" points="1776.0217,-102.1481 1765.9793,-105.5244 1775.9353,-109.1476 1776.0217,-102.1481"/>
<text text-anchor="middle" x="3162.5894" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel3 -->
<g id="node78" class="node">
<title>BulkRNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="6663.5894" cy="-453" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="6663.5894" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel3</text>
</g>
<!-- BulkRNA_seqLevel3&#45;&gt;BulkRNA_seqLevel2 -->
<g id="edge59" class="edge">
<title>BulkRNA_seqLevel3&#45;&gt;BulkRNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M6663.5894,-434.9735C6663.5894,-423.1918 6663.5894,-407.5607 6663.5894,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="6667.0895,-394.0033 6663.5894,-384.0034 6660.0895,-394.0034 6667.0895,-394.0033"/>
<text text-anchor="middle" x="6737.5894" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
</g>
</svg>
</div>