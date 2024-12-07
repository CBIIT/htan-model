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
<svg width="6027pt" height="653pt"
 viewBox="0.00 0.00 6026.99 653.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 649)">
<title>Perl</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-649 6022.9919,-649 6022.9919,4 -4,4"/>
<!-- ScATAC_seqLevel4 -->
<g id="node1" class="node">
<title>ScATAC_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="300.9919" cy="-540" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="300.9919" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel4</text>
</g>
<!-- ScATAC_seqLevel3 -->
<g id="node15" class="node">
<title>ScATAC_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="300.9919" cy="-453" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="300.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel3</text>
</g>
<!-- ScATAC_seqLevel4&#45;&gt;ScATAC_seqLevel3 -->
<g id="edge13" class="edge">
<title>ScATAC_seqLevel4&#45;&gt;ScATAC_seqLevel3</title>
<path fill="none" stroke="#000000" d="M300.9919,-521.9735C300.9919,-510.1918 300.9919,-494.5607 300.9919,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="304.492,-481.0033 300.9919,-471.0034 297.492,-481.0034 304.492,-481.0033"/>
<text text-anchor="middle" x="374.9919" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Biospecimen -->
<g id="node2" class="node">
<title>Biospecimen</title>
<ellipse fill="none" stroke="#000000" cx="2108.9919" cy="-192" rx="70.3881" ry="18"/>
<text text-anchor="middle" x="2108.9919" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">Biospecimen</text>
</g>
<!-- Patient -->
<g id="node43" class="node">
<title>Patient</title>
<ellipse fill="none" stroke="#000000" cx="2200.9919" cy="-105" rx="44.393" ry="18"/>
<text text-anchor="middle" x="2200.9919" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">Patient</text>
</g>
<!-- Biospecimen&#45;&gt;Patient -->
<g id="edge17" class="edge">
<title>Biospecimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2110.6341,-173.7115C2112.4275,-163.1101 2116.1735,-150.1007 2123.9919,-141 2132.1057,-131.5555 2143.2355,-124.426 2154.5119,-119.1114"/>
<polygon fill="#000000" stroke="#000000" points="2156.1434,-122.2201 2163.9555,-115.063 2153.3853,-115.7863 2156.1434,-122.2201"/>
<text text-anchor="middle" x="2197.9919" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScmC_seqLevel1 -->
<g id="node3" class="node">
<title>ScmC_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="90.9919" cy="-279" rx="90.9839" ry="18"/>
<text text-anchor="middle" x="90.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScmC_seqLevel1</text>
</g>
<!-- ScmC_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge10" class="edge">
<title>ScmC_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M104.7485,-261.0118C114.9575,-249.2098 130.0076,-234.7547 146.9919,-228 191.3791,-210.3471 1664.7349,-195.9871 2028.4426,-192.7055"/>
<polygon fill="#000000" stroke="#000000" points="2028.6536,-196.2039 2038.6217,-192.614 2028.5906,-189.2041 2028.6536,-196.2039"/>
<text text-anchor="middle" x="220.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel1 -->
<g id="node4" class="node">
<title>ScATAC_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="300.9919" cy="-279" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="300.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel1</text>
</g>
<!-- ScATAC_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge12" class="edge">
<title>ScATAC_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M297.3539,-260.8075C296.2811,-249.6895 297.2409,-236.0957 305.9919,-228 338.0226,-198.368 1682.3175,-193.0436 2028.4105,-192.1632"/>
<polygon fill="#000000" stroke="#000000" points="2028.6088,-195.6629 2038.6,-192.1379 2028.5913,-188.6629 2028.6088,-195.6629"/>
<text text-anchor="middle" x="379.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel3 -->
<g id="node5" class="node">
<title>Slide_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="5870.9919" cy="-453" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="5870.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel3</text>
</g>
<!-- Slide_seqLevel2 -->
<g id="node66" class="node">
<title>Slide_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="5870.9919" cy="-366" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="5870.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel2</text>
</g>
<!-- Slide_seqLevel3&#45;&gt;Slide_seqLevel2 -->
<g id="edge8" class="edge">
<title>Slide_seqLevel3&#45;&gt;Slide_seqLevel2</title>
<path fill="none" stroke="#000000" d="M5870.9919,-434.9735C5870.9919,-423.1918 5870.9919,-407.5607 5870.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="5874.492,-394.0033 5870.9919,-384.0034 5867.492,-394.0034 5874.492,-394.0033"/>
<text text-anchor="middle" x="5944.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel4 -->
<g id="node6" class="node">
<title>ImagingLevel4</title>
<ellipse fill="none" stroke="#000000" cx="5452.9919" cy="-453" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="5452.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel4</text>
</g>
<!-- ImagingLevel3Channels -->
<g id="node8" class="node">
<title>ImagingLevel3Channels</title>
<ellipse fill="none" stroke="#000000" cx="5430.9919" cy="-366" rx="124.2781" ry="18"/>
<text text-anchor="middle" x="5430.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Channels</text>
</g>
<!-- ImagingLevel4&#45;&gt;ImagingLevel3Channels -->
<g id="edge9" class="edge">
<title>ImagingLevel4&#45;&gt;ImagingLevel3Channels</title>
<path fill="none" stroke="#000000" d="M5448.4335,-434.9735C5445.4247,-423.0751 5441.4232,-407.2508 5438.0119,-393.7606"/>
<polygon fill="#000000" stroke="#000000" points="5441.3893,-392.8401 5435.5445,-384.0034 5434.6029,-394.5563 5441.3893,-392.8401"/>
<text text-anchor="middle" x="5516.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles -->
<g id="node7" class="node">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</title>
<ellipse fill="none" stroke="#000000" cx="2494.9919" cy="-453" rx="243.1569" ry="18"/>
<text text-anchor="middle" x="2494.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="node32" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2485.9919" cy="-279" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="2485.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="edge37" class="edge">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M2517.7929,-434.8934C2522.7458,-429.6966 2527.3031,-423.6229 2529.9919,-417 2547.0449,-374.9963 2549.405,-355.9664 2529.9919,-315 2528.1375,-311.0867 2525.6263,-307.4574 2522.7379,-304.1296"/>
<polygon fill="#000000" stroke="#000000" points="2525.0176,-301.4616 2515.4454,-296.9203 2520.0963,-306.4397 2525.0176,-301.4616"/>
<text text-anchor="middle" x="2617.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="node46" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2254.9919" cy="-366" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="2254.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="edge36" class="edge">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M2437.231,-435.497C2419.4246,-429.8606 2399.8173,-423.4088 2381.9919,-417 2356.95,-407.9967 2329.5112,-397.1095 2306.5659,-387.7102"/>
<polygon fill="#000000" stroke="#000000" points="2307.6069,-384.3538 2297.0275,-383.7829 2304.9418,-390.8266 2307.6069,-384.3538"/>
<text text-anchor="middle" x="2455.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel2 -->
<g id="node9" class="node">
<title>BulkMethylation_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="635.9919" cy="-366" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="635.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel2</text>
</g>
<!-- BulkMethylation_seqLevel2&#45;&gt;Biospecimen -->
<g id="edge32" class="edge">
<title>BulkMethylation_seqLevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M632.6801,-347.7384C629.9718,-337.1465 625.2005,-324.1377 616.9919,-315 605.0375,-301.6924 590.3965,-312.2169 580.9919,-297 572.5802,-283.3896 570.2488,-272.8569 580.9919,-261 629.9423,-206.9749 1719.5792,-194.8623 2028.1977,-192.511"/>
<polygon fill="#000000" stroke="#000000" points="2028.4351,-196.0094 2038.4086,-192.4346 2028.3827,-189.0096 2028.4351,-196.0094"/>
<text text-anchor="middle" x="654.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel1 -->
<g id="node29" class="node">
<title>BulkMethylation_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1027.9919" cy="-279" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="1027.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel1</text>
</g>
<!-- BulkMethylation_seqLevel2&#45;&gt;BulkMethylation_seqLevel1 -->
<g id="edge31" class="edge">
<title>BulkMethylation_seqLevel2&#45;&gt;BulkMethylation_seqLevel1</title>
<path fill="none" stroke="#000000" d="M706.5264,-350.3457C774.4211,-335.2772 876.9673,-312.5182 947.9017,-296.7751"/>
<polygon fill="#000000" stroke="#000000" points="948.69,-300.1854 957.6941,-294.6018 947.1733,-293.3517 948.69,-300.1854"/>
<text text-anchor="middle" x="929.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel1 -->
<g id="node10" class="node">
<title>MassSpectrometryLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1469.9919" cy="-279" rx="130.777" ry="18"/>
<text text-anchor="middle" x="1469.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel1</text>
</g>
<!-- MassSpectrometryLevel1&#45;&gt;Biospecimen -->
<g id="edge30" class="edge">
<title>MassSpectrometryLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1506.3495,-261.7001C1532.5862,-250.0568 1569.1943,-235.508 1602.9919,-228 1681.9108,-210.4685 1907.8708,-199.5676 2029.385,-194.8035"/>
<polygon fill="#000000" stroke="#000000" points="2029.523,-198.3008 2039.38,-194.4162 2029.2519,-191.3061 2029.523,-198.3008"/>
<text text-anchor="middle" x="1676.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel4 -->
<g id="node11" class="node">
<title>ElectronMicroscopyLevel4</title>
<ellipse fill="none" stroke="#000000" cx="3122.9919" cy="-540" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3122.9919" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel4</text>
</g>
<!-- ElectronMicroscopyLevel3 -->
<g id="node30" class="node">
<title>ElectronMicroscopyLevel3</title>
<ellipse fill="none" stroke="#000000" cx="3122.9919" cy="-453" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3122.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel3</text>
</g>
<!-- ElectronMicroscopyLevel4&#45;&gt;ElectronMicroscopyLevel3 -->
<g id="edge33" class="edge">
<title>ElectronMicroscopyLevel4&#45;&gt;ElectronMicroscopyLevel3</title>
<path fill="none" stroke="#000000" d="M3122.9919,-521.9735C3122.9919,-510.1918 3122.9919,-494.5607 3122.9919,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="3126.492,-481.0033 3122.9919,-471.0034 3119.492,-481.0034 3126.492,-481.0033"/>
<text text-anchor="middle" x="3196.9919" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Exposure -->
<g id="node12" class="node">
<title>Exposure</title>
<ellipse fill="none" stroke="#000000" cx="1687.9919" cy="-18" rx="54.6905" ry="18"/>
<text text-anchor="middle" x="1687.9919" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Exposure</text>
</g>
<!-- OtherAssay -->
<g id="node13" class="node">
<title>OtherAssay</title>
<ellipse fill="none" stroke="#000000" cx="803.9919" cy="-279" rx="65.7887" ry="18"/>
<text text-anchor="middle" x="803.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">OtherAssay</text>
</g>
<!-- OtherAssay&#45;&gt;Biospecimen -->
<g id="edge23" class="edge">
<title>OtherAssay&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M844.112,-264.5787C880.1821,-252.3525 934.8858,-235.6249 983.9919,-228 1086.1937,-212.1308 1788.7552,-197.8881 2028.7981,-193.4349"/>
<polygon fill="#000000" stroke="#000000" points="2028.9187,-196.9333 2038.8523,-193.249 2028.7893,-189.9345 2028.9187,-196.9333"/>
<text text-anchor="middle" x="1057.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel1 -->
<g id="node14" class="node">
<title>HI_C_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1705.9919" cy="-279" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="1705.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel1</text>
</g>
<!-- HI_C_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge22" class="edge">
<title>HI_C_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1727.0367,-261.2911C1741.9535,-249.7753 1762.9777,-235.5447 1783.9919,-228 1827.8004,-212.2714 1948.8419,-201.9215 2030.1937,-196.5133"/>
<polygon fill="#000000" stroke="#000000" points="2030.6544,-199.9907 2040.405,-195.8464 2030.1982,-193.0056 2030.6544,-199.9907"/>
<text text-anchor="middle" x="1857.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel2 -->
<g id="node27" class="node">
<title>ScATAC_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="300.9919" cy="-366" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="300.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel2</text>
</g>
<!-- ScATAC_seqLevel3&#45;&gt;ScATAC_seqLevel2 -->
<g id="edge24" class="edge">
<title>ScATAC_seqLevel3&#45;&gt;ScATAC_seqLevel2</title>
<path fill="none" stroke="#000000" d="M300.9919,-434.9735C300.9919,-423.1918 300.9919,-407.5607 300.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="304.492,-394.0033 300.9919,-384.0034 297.492,-394.0034 304.492,-394.0033"/>
<text text-anchor="middle" x="374.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3 -->
<g id="node16" class="node">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3</title>
<ellipse fill="none" stroke="#000000" cx="4392.9919" cy="-453" rx="258.0542" ry="18"/>
<text text-anchor="middle" x="4392.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPSpatialTranscriptomicsLevel3</text>
</g>
<!-- NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="node37" class="node">
<title>NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<ellipse fill="none" stroke="#000000" cx="3571.9919" cy="-279" rx="295.1477" ry="18"/>
<text text-anchor="middle" x="3571.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="edge28" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M4222.1361,-439.4899C4074.372,-426.6679 3872.6367,-406.1144 3794.9919,-384 3727.1761,-364.6851 3654.2711,-326.7325 3610.9251,-302.1375"/>
<polygon fill="#000000" stroke="#000000" points="3612.5537,-299.0368 3602.1367,-297.1035 3609.0744,-305.111 3612.5537,-299.0368"/>
<text text-anchor="middle" x="3868.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1 -->
<g id="node39" class="node">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</title>
<ellipse fill="none" stroke="#000000" cx="4209.9919" cy="-366" rx="258.0542" ry="18"/>
<text text-anchor="middle" x="4209.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPSpatialTranscriptomicsLevel1 -->
<g id="edge27" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</title>
<path fill="none" stroke="#000000" d="M4355.5176,-435.1843C4326.9932,-421.6236 4287.5556,-402.8745 4256.93,-388.3148"/>
<polygon fill="#000000" stroke="#000000" points="4258.2643,-385.0738 4247.7302,-383.9411 4255.2588,-391.3958 4258.2643,-385.0738"/>
<text text-anchor="middle" x="4386.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel2 -->
<g id="node60" class="node">
<title>ImagingLevel2</title>
<ellipse fill="none" stroke="#000000" cx="4996.9919" cy="-366" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="4996.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel2</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;ImagingLevel2 -->
<g id="edge26" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M4514.8842,-437.1014C4654.8528,-418.7767 4870.127,-390.3584 4907.9919,-384 4914.5725,-382.895 4921.4101,-381.6633 4928.2398,-380.377"/>
<polygon fill="#000000" stroke="#000000" points="4929.0495,-383.7855 4938.2097,-378.4618 4927.7289,-376.9112 4929.0495,-383.7855"/>
<text text-anchor="middle" x="4845.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="node64" class="node">
<title>NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<ellipse fill="none" stroke="#000000" cx="4178.9919" cy="-279" rx="294.3478" ry="18"/>
<text text-anchor="middle" x="4178.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="edge29" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M4441.4779,-435.1689C4450.1503,-430.3041 4458.483,-424.3032 4464.9919,-417 4485.7022,-393.7627 4496.0577,-372.6046 4476.9919,-348 4458.1191,-323.6444 4395.1256,-307.1916 4331.8881,-296.4814"/>
<polygon fill="#000000" stroke="#000000" points="4332.1793,-292.9823 4321.7435,-294.8114 4331.0422,-299.8893 4332.1793,-292.9823"/>
<text text-anchor="middle" x="4561.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Segmentation -->
<g id="node17" class="node">
<title>ImagingLevel3Segmentation</title>
<ellipse fill="none" stroke="#000000" cx="4939.9919" cy="-453" rx="145.6742" ry="18"/>
<text text-anchor="middle" x="4939.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Segmentation</text>
</g>
<!-- ImagingLevel3Segmentation&#45;&gt;ImagingLevel2 -->
<g id="edge20" class="edge">
<title>ImagingLevel3Segmentation&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M4936.3451,-434.9217C4935.2128,-424.6456 4935.4628,-411.8956 4940.9919,-402 4943.8812,-396.829 4947.858,-392.2857 4952.3711,-388.3258"/>
<polygon fill="#000000" stroke="#000000" points="4954.5578,-391.0597 4960.3753,-382.2049 4950.3056,-385.4992 4954.5578,-391.0597"/>
<text text-anchor="middle" x="5014.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel4 -->
<g id="node18" class="node">
<title>ScRNA_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="5669.9919" cy="-540" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="5669.9919" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel4</text>
</g>
<!-- ScRNA_seqLevel3 -->
<g id="node31" class="node">
<title>ScRNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="5669.9919" cy="-453" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="5669.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel3</text>
</g>
<!-- ScRNA_seqLevel4&#45;&gt;ScRNA_seqLevel3 -->
<g id="edge21" class="edge">
<title>ScRNA_seqLevel4&#45;&gt;ScRNA_seqLevel3</title>
<path fill="none" stroke="#000000" d="M5669.9919,-521.9735C5669.9919,-510.1918 5669.9919,-494.5607 5669.9919,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="5673.492,-481.0033 5669.9919,-471.0034 5666.492,-481.0034 5673.492,-481.0033"/>
<text text-anchor="middle" x="5743.9919" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel3 -->
<g id="node19" class="node">
<title>HI_C_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="1705.9919" cy="-453" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="1705.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel3</text>
</g>
<!-- HI_C_seqLevel2 -->
<g id="node55" class="node">
<title>HI_C_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1705.9919" cy="-366" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="1705.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel2</text>
</g>
<!-- HI_C_seqLevel3&#45;&gt;HI_C_seqLevel2 -->
<g id="edge52" class="edge">
<title>HI_C_seqLevel3&#45;&gt;HI_C_seqLevel2</title>
<path fill="none" stroke="#000000" d="M1705.9919,-434.9735C1705.9919,-423.1918 1705.9919,-407.5607 1705.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="1709.492,-394.0033 1705.9919,-384.0034 1702.492,-394.0034 1709.492,-394.0033"/>
<text text-anchor="middle" x="1779.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- FollowUp -->
<g id="node20" class="node">
<title>FollowUp</title>
<ellipse fill="none" stroke="#000000" cx="1858.9919" cy="-18" rx="54.6905" ry="18"/>
<text text-anchor="middle" x="1858.9919" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">FollowUp</text>
</g>
<!-- RPPALevel3 -->
<g id="node21" class="node">
<title>RPPALevel3</title>
<ellipse fill="none" stroke="#000000" cx="1253.9919" cy="-279" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="1253.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel3</text>
</g>
<!-- RPPALevel3&#45;&gt;Biospecimen -->
<g id="edge57" class="edge">
<title>RPPALevel3&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1289.6569,-263.6377C1319.3715,-251.6132 1363.1234,-235.6826 1402.9919,-228 1520.6933,-205.3191 1869.8206,-196.2909 2028.6752,-193.2857"/>
<polygon fill="#000000" stroke="#000000" points="2028.9259,-196.7817 2038.8591,-193.0964 2028.7957,-189.7829 2028.9259,-196.7817"/>
<text text-anchor="middle" x="1476.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel2 -->
<g id="node22" class="node">
<title>BulkWESLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1897.9919" cy="-366" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="1897.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel2</text>
</g>
<!-- BulkWESLevel1 -->
<g id="node24" class="node">
<title>BulkWESLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1897.9919" cy="-279" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="1897.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel1</text>
</g>
<!-- BulkWESLevel2&#45;&gt;BulkWESLevel1 -->
<g id="edge59" class="edge">
<title>BulkWESLevel2&#45;&gt;BulkWESLevel1</title>
<path fill="none" stroke="#000000" d="M1897.9919,-347.9735C1897.9919,-336.1918 1897.9919,-320.5607 1897.9919,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1901.492,-307.0033 1897.9919,-297.0034 1894.492,-307.0034 1901.492,-307.0033"/>
<text text-anchor="middle" x="1971.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel3 -->
<g id="node23" class="node">
<title>BulkRNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="2862.9919" cy="-453" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="2862.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel3</text>
</g>
<!-- BulkRNA_seqLevel2 -->
<g id="node53" class="node">
<title>BulkRNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2862.9919" cy="-366" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="2862.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel2</text>
</g>
<!-- BulkRNA_seqLevel3&#45;&gt;BulkRNA_seqLevel2 -->
<g id="edge58" class="edge">
<title>BulkRNA_seqLevel3&#45;&gt;BulkRNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M2862.9919,-434.9735C2862.9919,-423.1918 2862.9919,-407.5607 2862.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="2866.492,-394.0033 2862.9919,-384.0034 2859.492,-394.0034 2866.492,-394.0033"/>
<text text-anchor="middle" x="2936.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel1&#45;&gt;Biospecimen -->
<g id="edge51" class="edge">
<title>BulkWESLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1914.4133,-260.9194C1925.4304,-249.8461 1940.8384,-236.2599 1956.9919,-228 1981.292,-215.5744 2009.9775,-207.3547 2035.8448,-201.9544"/>
<polygon fill="#000000" stroke="#000000" points="2036.8494,-205.3236 2045.9801,-199.9496 2035.491,-198.4567 2036.8494,-205.3236"/>
<text text-anchor="middle" x="2030.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel3 -->
<g id="node25" class="node">
<title>MassSpectrometryLevel3</title>
<ellipse fill="none" stroke="#000000" cx="1469.9919" cy="-453" rx="130.777" ry="18"/>
<text text-anchor="middle" x="1469.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel3</text>
</g>
<!-- MassSpectrometryLevel2 -->
<g id="node49" class="node">
<title>MassSpectrometryLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1469.9919" cy="-366" rx="130.777" ry="18"/>
<text text-anchor="middle" x="1469.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel2</text>
</g>
<!-- MassSpectrometryLevel3&#45;&gt;MassSpectrometryLevel2 -->
<g id="edge49" class="edge">
<title>MassSpectrometryLevel3&#45;&gt;MassSpectrometryLevel2</title>
<path fill="none" stroke="#000000" d="M1469.9919,-434.9735C1469.9919,-423.1918 1469.9919,-407.5607 1469.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="1473.492,-394.0033 1469.9919,-384.0034 1466.492,-394.0034 1473.492,-394.0033"/>
<text text-anchor="middle" x="1543.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3 -->
<g id="node26" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="2195.9919" cy="-540" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="2195.9919" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_AuxiliaryFiles -->
<g id="edge42" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</title>
<path fill="none" stroke="#000000" d="M2256.1394,-522.4989C2305.0027,-508.2811 2373.9814,-488.2104 2425.2573,-473.2907"/>
<polygon fill="#000000" stroke="#000000" points="2426.3167,-476.6277 2434.9406,-470.4731 2424.3609,-469.9064 2426.3167,-476.6277"/>
<text text-anchor="middle" x="2437.9919" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="edge41" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M2156.7182,-522.134C2119.4766,-502.5946 2072.3348,-469.445 2094.9919,-435 2109.954,-412.2535 2134.1719,-396.9725 2159.2881,-386.7191"/>
<polygon fill="#000000" stroke="#000000" points="2160.8489,-389.8696 2168.9407,-383.0305 2158.3502,-383.3308 2160.8489,-389.8696"/>
<text text-anchor="middle" x="2168.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel2&#45;&gt;ScATAC_seqLevel1 -->
<g id="edge44" class="edge">
<title>ScATAC_seqLevel2&#45;&gt;ScATAC_seqLevel1</title>
<path fill="none" stroke="#000000" d="M299.171,-347.7043C298.6866,-342.0358 298.2317,-335.7649 297.9919,-330 297.6898,-322.7361 297.8887,-314.8952 298.2988,-307.5916"/>
<polygon fill="#000000" stroke="#000000" points="301.8049,-307.6265 299.0169,-297.4051 294.8222,-307.1342 301.8049,-307.6265"/>
<text text-anchor="middle" x="371.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel2 -->
<g id="node28" class="node">
<title>ElectronMicroscopyLevel2</title>
<ellipse fill="none" stroke="#000000" cx="3122.9919" cy="-366" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3122.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel2</text>
</g>
<!-- ElectronMicroscopyLevel1 -->
<g id="node54" class="node">
<title>ElectronMicroscopyLevel1</title>
<ellipse fill="none" stroke="#000000" cx="3122.9919" cy="-279" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3122.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel1</text>
</g>
<!-- ElectronMicroscopyLevel2&#45;&gt;ElectronMicroscopyLevel1 -->
<g id="edge45" class="edge">
<title>ElectronMicroscopyLevel2&#45;&gt;ElectronMicroscopyLevel1</title>
<path fill="none" stroke="#000000" d="M3122.9919,-347.9735C3122.9919,-336.1918 3122.9919,-320.5607 3122.9919,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="3126.492,-307.0033 3122.9919,-297.0034 3119.492,-307.0034 3126.492,-307.0033"/>
<text text-anchor="middle" x="3196.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge46" class="edge">
<title>BulkMethylation_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1073.1511,-261.9518C1106.7698,-250.1064 1154.0731,-235.2026 1196.9919,-228 1355.6978,-201.3663 1836.6817,-194.3335 2028.6315,-192.5644"/>
<polygon fill="#000000" stroke="#000000" points="2028.6857,-196.0641 2038.6538,-192.4744 2028.6228,-189.0644 2028.6857,-196.0641"/>
<text text-anchor="middle" x="1270.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel3&#45;&gt;ElectronMicroscopyLevel2 -->
<g id="edge47" class="edge">
<title>ElectronMicroscopyLevel3&#45;&gt;ElectronMicroscopyLevel2</title>
<path fill="none" stroke="#000000" d="M3122.9919,-434.9735C3122.9919,-423.1918 3122.9919,-407.5607 3122.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="3126.492,-394.0033 3122.9919,-384.0034 3119.492,-394.0034 3126.492,-394.0033"/>
<text text-anchor="middle" x="3196.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel2 -->
<g id="node65" class="node">
<title>ScRNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="5669.9919" cy="-366" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="5669.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel2</text>
</g>
<!-- ScRNA_seqLevel3&#45;&gt;ScRNA_seqLevel2 -->
<g id="edge38" class="edge">
<title>ScRNA_seqLevel3&#45;&gt;ScRNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M5669.9919,-434.9735C5669.9919,-423.1918 5669.9919,-407.5607 5669.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="5673.492,-394.0033 5669.9919,-384.0034 5666.492,-394.0034 5673.492,-394.0033"/>
<text text-anchor="middle" x="5743.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge66" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2411.0581,-261.7076C2340.796,-245.4932 2236.972,-221.5339 2171.1786,-206.3508"/>
<polygon fill="#000000" stroke="#000000" points="2171.8874,-202.9224 2161.3564,-204.0841 2170.3133,-209.7432 2171.8874,-202.9224"/>
<text text-anchor="middle" x="2394.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Image -->
<g id="node33" class="node">
<title>ImagingLevel3Image</title>
<ellipse fill="none" stroke="#000000" cx="5228.9919" cy="-453" rx="109.6807" ry="18"/>
<text text-anchor="middle" x="5228.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Image</text>
</g>
<!-- ImagingLevel3Image&#45;&gt;ImagingLevel3Channels -->
<g id="edge67" class="edge">
<title>ImagingLevel3Image&#45;&gt;ImagingLevel3Channels</title>
<path fill="none" stroke="#000000" d="M5245.4531,-434.9967C5256.4861,-423.9542 5271.8969,-410.3733 5287.9919,-402 5303.897,-393.7255 5321.8015,-387.2841 5339.4212,-382.292"/>
<polygon fill="#000000" stroke="#000000" points="5340.4216,-385.6474 5349.1661,-379.6654 5338.5998,-378.8886 5340.4216,-385.6474"/>
<text text-anchor="middle" x="5361.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Image&#45;&gt;ImagingLevel2 -->
<g id="edge68" class="edge">
<title>ImagingLevel3Image&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M5170.6741,-437.6712C5152.2036,-432.0457 5131.933,-425.0529 5113.9919,-417 5102.1705,-411.6939 5100.6216,-407.7142 5088.9919,-402 5076.481,-395.8527 5062.6411,-389.9802 5049.5772,-384.8276"/>
<polygon fill="#000000" stroke="#000000" points="5050.821,-381.5561 5040.2318,-381.2093 5048.2935,-388.0839 5050.821,-381.5561"/>
<text text-anchor="middle" x="5187.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SRRSImagingLevel2 -->
<g id="node34" class="node">
<title>SRRSImagingLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2108.9919" cy="-279" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="2108.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSImagingLevel2</text>
</g>
<!-- SRRSImagingLevel2&#45;&gt;Biospecimen -->
<g id="edge64" class="edge">
<title>SRRSImagingLevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2108.9919,-260.9735C2108.9919,-249.1918 2108.9919,-233.5607 2108.9919,-220.1581"/>
<polygon fill="#000000" stroke="#000000" points="2112.492,-220.0033 2108.9919,-210.0034 2105.492,-220.0034 2112.492,-220.0033"/>
<text text-anchor="middle" x="2182.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel1 -->
<g id="node35" class="node">
<title>BulkRNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2862.9919" cy="-279" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="2862.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel1</text>
</g>
<!-- BulkRNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge62" class="edge">
<title>BulkRNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2785.7237,-266.5167C2773.1241,-264.5932 2760.2029,-262.6878 2747.9919,-261 2626.0521,-244.146 2595.5788,-239.2174 2472.9919,-228 2346.6009,-216.4345 2313.6056,-228.1566 2187.9919,-210 2181.8706,-209.1152 2175.5215,-208.0033 2169.2035,-206.7685"/>
<polygon fill="#000000" stroke="#000000" points="2169.8378,-203.3258 2159.338,-204.7419 2168.4292,-210.1826 2169.8378,-203.3258"/>
<text text-anchor="middle" x="2689.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Diagnosis -->
<g id="node36" class="node">
<title>Diagnosis</title>
<ellipse fill="none" stroke="#000000" cx="2029.9919" cy="-18" rx="55.7903" ry="18"/>
<text text-anchor="middle" x="2029.9919" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Diagnosis</text>
</g>
<!-- BulkMethylation_seqLevel3 -->
<g id="node38" class="node">
<title>BulkMethylation_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="579.9919" cy="-453" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="579.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel3</text>
</g>
<!-- BulkMethylation_seqLevel3&#45;&gt;Biospecimen -->
<g id="edge19" class="edge">
<title>BulkMethylation_seqLevel3&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M546.0499,-435.3597C502.5941,-410.3229 436.1573,-362.2536 464.9919,-315 511.2753,-239.1517 558.2703,-247.3513 644.9919,-228 779.8034,-197.9178 1740.7019,-192.9665 2028.0365,-192.157"/>
<polygon fill="#000000" stroke="#000000" points="2028.3872,-195.6561 2038.3776,-192.1288 2028.3681,-188.6561 2028.3872,-195.6561"/>
<text text-anchor="middle" x="538.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel3&#45;&gt;BulkMethylation_seqLevel2 -->
<g id="edge18" class="edge">
<title>BulkMethylation_seqLevel3&#45;&gt;BulkMethylation_seqLevel2</title>
<path fill="none" stroke="#000000" d="M591.5952,-434.9735C599.4792,-422.7252 610.0411,-406.3165 618.8852,-392.5766"/>
<polygon fill="#000000" stroke="#000000" points="621.9341,-394.3064 624.4036,-384.0034 616.048,-390.5176 621.9341,-394.3064"/>
<text text-anchor="middle" x="685.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;Biospecimen -->
<g id="edge16" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M4361.6773,-351.4074C4448.2599,-337.4712 4530.726,-310.8684 4481.9919,-261 4426.2961,-204.0078 3127.6605,-229.7504 3047.9919,-228 2856.8851,-223.8011 2377.713,-233.3531 2187.9919,-210 2181.67,-209.2218 2175.1129,-208.1558 2168.6016,-206.9281"/>
<polygon fill="#000000" stroke="#000000" points="2168.9418,-203.4264 2158.4476,-204.8838 2167.5601,-210.2887 2168.9418,-203.4264"/>
<text text-anchor="middle" x="4570.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="edge15" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M4092.2294,-349.9415C3981.8737,-334.893 3817.2106,-312.4389 3702.8073,-296.8385"/>
<polygon fill="#000000" stroke="#000000" points="3702.9703,-293.3284 3692.5891,-295.4451 3702.0245,-300.2642 3702.9703,-293.3284"/>
<text text-anchor="middle" x="4003.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="edge14" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M4203.5687,-347.9735C4199.329,-336.0751 4193.6905,-320.2508 4188.8836,-306.7606"/>
<polygon fill="#000000" stroke="#000000" points="4192.0604,-305.2484 4185.4069,-297.0034 4185.4665,-307.598 4192.0604,-305.2484"/>
<text text-anchor="middle" x="4270.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Demographics -->
<g id="node40" class="node">
<title>Demographics</title>
<ellipse fill="none" stroke="#000000" cx="2200.9919" cy="-18" rx="77.9862" ry="18"/>
<text text-anchor="middle" x="2200.9919" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Demographics</text>
</g>
<!-- SRRSBiospecimen -->
<g id="node41" class="node">
<title>SRRSBiospecimen</title>
<ellipse fill="none" stroke="#000000" cx="2293.9919" cy="-192" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="2293.9919" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSBiospecimen</text>
</g>
<!-- SRRSBiospecimen&#45;&gt;Patient -->
<g id="edge11" class="edge">
<title>SRRSBiospecimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2289.4889,-173.7361C2286.116,-163.1434 2280.577,-150.1346 2271.9919,-141 2264.3106,-132.827 2254.3641,-126.2179 2244.3604,-121.0027"/>
<polygon fill="#000000" stroke="#000000" points="2245.749,-117.7866 2235.2208,-116.6001 2242.7111,-124.0931 2245.749,-117.7866"/>
<text text-anchor="middle" x="2356.9919" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Therapy -->
<g id="node42" class="node">
<title>Therapy</title>
<ellipse fill="none" stroke="#000000" cx="2371.9919" cy="-18" rx="49.2915" ry="18"/>
<text text-anchor="middle" x="2371.9919" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Therapy</text>
</g>
<!-- Patient&#45;&gt;Exposure -->
<g id="edge5" class="edge">
<title>Patient&#45;&gt;Exposure</title>
<path fill="none" stroke="#000000" d="M2156.745,-103.8738C2045.2447,-100.7269 1758.9816,-90.6185 1721.9919,-69 1712.5519,-63.4828 1705.2125,-54.1786 1699.8082,-45.0161"/>
<polygon fill="#000000" stroke="#000000" points="1702.8254,-43.2353 1695.0427,-36.0464 1696.6437,-46.5196 1702.8254,-43.2353"/>
<text text-anchor="middle" x="1795.9919" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;FollowUp -->
<g id="edge2" class="edge">
<title>Patient&#45;&gt;FollowUp</title>
<path fill="none" stroke="#000000" d="M2157.2952,-102.2143C2076.279,-96.7268 1908.9702,-83.7612 1886.9919,-69 1878.6173,-63.3753 1872.5153,-54.3769 1868.1875,-45.4933"/>
<polygon fill="#000000" stroke="#000000" points="1871.3078,-43.8879 1864.164,-36.0638 1864.8694,-46.6351 1871.3078,-43.8879"/>
<text text-anchor="middle" x="1960.9919" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Diagnosis -->
<g id="edge1" class="edge">
<title>Patient&#45;&gt;Diagnosis</title>
<path fill="none" stroke="#000000" d="M2158.6523,-99.5023C2119.53,-93.636 2065.1017,-83.2256 2048.9919,-69 2042.1706,-62.9764 2037.7926,-54.2666 2034.985,-45.7444"/>
<polygon fill="#000000" stroke="#000000" points="2038.34,-44.7429 2032.3582,-35.9983 2031.5812,-46.5647 2038.34,-44.7429"/>
<text text-anchor="middle" x="2122.9919" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Demographics -->
<g id="edge4" class="edge">
<title>Patient&#45;&gt;Demographics</title>
<path fill="none" stroke="#000000" d="M2200.9919,-86.9735C2200.9919,-75.1918 2200.9919,-59.5607 2200.9919,-46.1581"/>
<polygon fill="#000000" stroke="#000000" points="2204.492,-46.0033 2200.9919,-36.0034 2197.492,-46.0034 2204.492,-46.0033"/>
<text text-anchor="middle" x="2274.9919" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Therapy -->
<g id="edge7" class="edge">
<title>Patient&#45;&gt;Therapy</title>
<path fill="none" stroke="#000000" d="M2243.0758,-99.1109C2281.2618,-93.0197 2333.967,-82.5059 2349.9919,-69 2357.0934,-63.0148 2361.9654,-54.3145 2365.2802,-45.7892"/>
<polygon fill="#000000" stroke="#000000" points="2368.689,-46.6278 2368.4966,-36.0347 2362.0411,-44.4357 2368.689,-46.6278"/>
<text text-anchor="middle" x="2435.9919" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- FamilyHistory -->
<g id="node47" class="node">
<title>FamilyHistory</title>
<ellipse fill="none" stroke="#000000" cx="2542.9919" cy="-18" rx="77.1866" ry="18"/>
<text text-anchor="middle" x="2542.9919" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">FamilyHistory</text>
</g>
<!-- Patient&#45;&gt;FamilyHistory -->
<g id="edge3" class="edge">
<title>Patient&#45;&gt;FamilyHistory</title>
<path fill="none" stroke="#000000" d="M2244.844,-102.1552C2325.6864,-96.5913 2492.0045,-83.5359 2513.9919,-69 2522.5682,-63.3302 2528.8899,-54.2029 2533.4015,-45.226"/>
<polygon fill="#000000" stroke="#000000" points="2536.6047,-46.6366 2537.4666,-36.0768 2530.2077,-43.7943 2536.6047,-46.6366"/>
<text text-anchor="middle" x="2602.9919" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MolecularTest -->
<g id="node48" class="node">
<title>MolecularTest</title>
<ellipse fill="none" stroke="#000000" cx="2715.9919" cy="-18" rx="77.1866" ry="18"/>
<text text-anchor="middle" x="2715.9919" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">MolecularTest</text>
</g>
<!-- Patient&#45;&gt;MolecularTest -->
<g id="edge6" class="edge">
<title>Patient&#45;&gt;MolecularTest</title>
<path fill="none" stroke="#000000" d="M2245.3141,-103.8495C2357.0067,-100.6449 2643.779,-90.4106 2680.9919,-69 2690.5559,-63.4973 2698.0809,-54.196 2703.6629,-45.0317"/>
<polygon fill="#000000" stroke="#000000" points="2706.8458,-46.5074 2708.6009,-36.0589 2700.7131,-43.1324 2706.8458,-46.5074"/>
<text text-anchor="middle" x="2771.9919" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScDNA_seqLevel2 -->
<g id="node44" class="node">
<title>ScDNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="5191.9919" cy="-366" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="5191.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScDNA_seqLevel2</text>
</g>
<!-- ScDNA_seqLevel1 -->
<g id="node63" class="node">
<title>ScDNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5278.9919" cy="-279" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="5278.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScDNA_seqLevel1</text>
</g>
<!-- ScDNA_seqLevel2&#45;&gt;ScDNA_seqLevel1 -->
<g id="edge35" class="edge">
<title>ScDNA_seqLevel2&#45;&gt;ScDNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M5210.0184,-347.9735C5222.7007,-335.2912 5239.8433,-318.1486 5253.8654,-304.1265"/>
<polygon fill="#000000" stroke="#000000" points="5256.69,-306.2517 5261.2862,-296.7057 5251.7403,-301.3019 5256.69,-306.2517"/>
<text text-anchor="middle" x="5313.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScmC_seqLevel2 -->
<g id="node45" class="node">
<title>ScmC_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="90.9919" cy="-366" rx="90.9839" ry="18"/>
<text text-anchor="middle" x="90.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScmC_seqLevel2</text>
</g>
<!-- ScmC_seqLevel2&#45;&gt;ScmC_seqLevel1 -->
<g id="edge34" class="edge">
<title>ScmC_seqLevel2&#45;&gt;ScmC_seqLevel1</title>
<path fill="none" stroke="#000000" d="M90.9919,-347.9735C90.9919,-336.1918 90.9919,-320.5607 90.9919,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="94.492,-307.0033 90.9919,-297.0034 87.492,-307.0034 94.492,-307.0033"/>
<text text-anchor="middle" x="164.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel2&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="edge25" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel2&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M2297.7034,-348.246C2322.2485,-338.1949 2353.7251,-325.5608 2381.9919,-315 2395.5163,-309.9471 2410.1176,-304.7407 2423.9818,-299.9116"/>
<polygon fill="#000000" stroke="#000000" points="2425.1366,-303.2157 2433.4401,-296.6351 2422.8453,-296.6013 2425.1366,-303.2157"/>
<text text-anchor="middle" x="2455.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel2&#45;&gt;MassSpectrometryLevel1 -->
<g id="edge53" class="edge">
<title>MassSpectrometryLevel2&#45;&gt;MassSpectrometryLevel1</title>
<path fill="none" stroke="#000000" d="M1469.9919,-347.9735C1469.9919,-336.1918 1469.9919,-320.5607 1469.9919,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1473.492,-307.0033 1469.9919,-297.0034 1466.492,-307.0034 1473.492,-307.0033"/>
<text text-anchor="middle" x="1543.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel3 -->
<g id="node50" class="node">
<title>BulkWESLevel3</title>
<ellipse fill="none" stroke="#000000" cx="1897.9919" cy="-453" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="1897.9919" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel3</text>
</g>
<!-- BulkWESLevel3&#45;&gt;BulkWESLevel2 -->
<g id="edge54" class="edge">
<title>BulkWESLevel3&#45;&gt;BulkWESLevel2</title>
<path fill="none" stroke="#000000" d="M1897.9919,-434.9735C1897.9919,-423.1918 1897.9919,-407.5607 1897.9919,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="1901.492,-394.0033 1897.9919,-384.0034 1894.492,-394.0034 1901.492,-394.0033"/>
<text text-anchor="middle" x="1971.9919" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel4 -->
<g id="node51" class="node">
<title>MassSpectrometryLevel4</title>
<ellipse fill="none" stroke="#000000" cx="1469.9919" cy="-540" rx="130.777" ry="18"/>
<text text-anchor="middle" x="1469.9919" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel4</text>
</g>
<!-- MassSpectrometryLevel4&#45;&gt;MassSpectrometryLevel3 -->
<g id="edge55" class="edge">
<title>MassSpectrometryLevel4&#45;&gt;MassSpectrometryLevel3</title>
<path fill="none" stroke="#000000" d="M1469.9919,-521.9735C1469.9919,-510.1918 1469.9919,-494.5607 1469.9919,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="1473.492,-481.0033 1469.9919,-471.0034 1466.492,-481.0034 1473.492,-481.0033"/>
<text text-anchor="middle" x="1543.9919" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel4 -->
<g id="node52" class="node">
<title>RPPALevel4</title>
<ellipse fill="none" stroke="#000000" cx="4830.9919" cy="-366" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="4830.9919" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel4</text>
</g>
<!-- RPPALevel2 -->
<g id="node59" class="node">
<title>RPPALevel2</title>
<ellipse fill="none" stroke="#000000" cx="4917.9919" cy="-279" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="4917.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel2</text>
</g>
<!-- RPPALevel4&#45;&gt;RPPALevel2 -->
<g id="edge56" class="edge">
<title>RPPALevel4&#45;&gt;RPPALevel2</title>
<path fill="none" stroke="#000000" d="M4831.0461,-347.8029C4831.9535,-337.2338 4834.6758,-324.2265 4841.9919,-315 4847.721,-307.775 4855.2488,-301.9239 4863.3393,-297.2084"/>
<polygon fill="#000000" stroke="#000000" points="4865.0455,-300.2658 4872.2806,-292.5261 4861.798,-294.0647 4865.0455,-300.2658"/>
<text text-anchor="middle" x="4915.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel2&#45;&gt;BulkRNA_seqLevel1 -->
<g id="edge60" class="edge">
<title>BulkRNA_seqLevel2&#45;&gt;BulkRNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M2862.9919,-347.9735C2862.9919,-336.1918 2862.9919,-320.5607 2862.9919,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="2866.492,-307.0033 2862.9919,-297.0034 2859.492,-307.0034 2866.492,-307.0033"/>
<text text-anchor="middle" x="2936.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel1&#45;&gt;Biospecimen -->
<g id="edge61" class="edge">
<title>ElectronMicroscopyLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M3041.1568,-264.5934C2969.3968,-252.5959 2862.1224,-236.1963 2767.9919,-228 2511.0622,-205.6281 2443.7996,-242.7996 2187.9919,-210 2181.674,-209.1899 2175.1195,-208.1033 2168.6098,-206.8632"/>
<polygon fill="#000000" stroke="#000000" points="2168.9534,-203.3618 2158.4574,-204.806 2167.5631,-210.2223 2168.9534,-203.3618"/>
<text text-anchor="middle" x="2969.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel2&#45;&gt;HI_C_seqLevel1 -->
<g id="edge50" class="edge">
<title>HI_C_seqLevel2&#45;&gt;HI_C_seqLevel1</title>
<path fill="none" stroke="#000000" d="M1705.9919,-347.9735C1705.9919,-336.1918 1705.9919,-320.5607 1705.9919,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1709.492,-307.0033 1705.9919,-297.0034 1702.492,-307.0034 1709.492,-307.0033"/>
<text text-anchor="middle" x="1779.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel1 -->
<g id="node56" class="node">
<title>ImagingLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5083.9919" cy="-279" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="5083.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel1</text>
</g>
<!-- ImagingLevel1&#45;&gt;Biospecimen -->
<g id="edge43" class="edge">
<title>ImagingLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5056.896,-261.811C5036.184,-249.7268 5006.4433,-234.5851 4977.9919,-228 4826.9807,-193.0484 2341.9671,-227.8227 2187.9919,-210 2181.42,-209.2393 2174.5965,-208.1506 2167.8356,-206.88"/>
<polygon fill="#000000" stroke="#000000" points="2168.5051,-203.4447 2158.0114,-204.9055 2167.1257,-210.3074 2168.5051,-203.4447"/>
<text text-anchor="middle" x="5094.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel1 -->
<g id="node57" class="node">
<title>ScRNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5572.9919" cy="-279" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="5572.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel1</text>
</g>
<!-- ScRNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge48" class="edge">
<title>ScRNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5524.0774,-263.4066C5482.7221,-251.0693 5421.649,-234.8223 5366.9919,-228 5016.4839,-184.2497 2538.893,-250.4766 2187.9919,-210 2181.4197,-209.2419 2174.596,-208.1548 2167.835,-206.8852"/>
<polygon fill="#000000" stroke="#000000" points="2168.5042,-203.4498 2158.0107,-204.9116 2167.1255,-210.3127 2168.5042,-203.4498"/>
<text text-anchor="middle" x="5520.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ExSeqMinimal -->
<g id="node58" class="node">
<title>ExSeqMinimal</title>
<ellipse fill="none" stroke="#000000" cx="4753.9919" cy="-279" rx="78.7863" ry="18"/>
<text text-anchor="middle" x="4753.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ExSeqMinimal</text>
</g>
<!-- ExSeqMinimal&#45;&gt;Biospecimen -->
<g id="edge39" class="edge">
<title>ExSeqMinimal&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M4704.4818,-264.9062C4658.048,-252.4463 4586.452,-235.1696 4522.9919,-228 4265.1799,-198.8729 2445.7045,-239.9945 2187.9919,-210 2181.4205,-209.2352 2174.5973,-208.1438 2167.8365,-206.8718"/>
<polygon fill="#000000" stroke="#000000" points="2168.5064,-203.4365 2158.0126,-204.8957 2167.126,-210.299 2168.5064,-203.4365"/>
<text text-anchor="middle" x="4686.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel2&#45;&gt;Biospecimen -->
<g id="edge40" class="edge">
<title>RPPALevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M4882.3311,-263.5442C4851.832,-251.2005 4806.4249,-234.8722 4764.9919,-228 4623.7514,-204.5733 2330.2081,-226.5 2187.9919,-210 2181.4202,-209.2375 2174.5968,-208.1477 2167.836,-206.8765"/>
<polygon fill="#000000" stroke="#000000" points="2168.5057,-203.4412 2158.0119,-204.9013 2167.1258,-210.3039 2168.5057,-203.4412"/>
<text text-anchor="middle" x="4899.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel2&#45;&gt;ImagingLevel1 -->
<g id="edge70" class="edge">
<title>ImagingLevel2&#45;&gt;ImagingLevel1</title>
<path fill="none" stroke="#000000" d="M5014.5977,-348.3943C5027.4513,-335.5407 5045.0473,-317.9446 5059.3041,-303.6878"/>
<polygon fill="#000000" stroke="#000000" points="5061.8161,-306.1255 5066.4124,-296.5796 5056.8664,-301.1758 5061.8161,-306.1255"/>
<text text-anchor="middle" x="5119.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel4 -->
<g id="node61" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="2195.9919" cy="-627" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="2195.9919" y="-623.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel4</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel4&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel3 -->
<g id="edge69" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel4&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</title>
<path fill="none" stroke="#000000" d="M2195.9919,-608.9735C2195.9919,-597.1918 2195.9919,-581.5607 2195.9919,-568.1581"/>
<polygon fill="#000000" stroke="#000000" points="2199.492,-568.0033 2195.9919,-558.0034 2192.492,-568.0034 2199.492,-568.0033"/>
<text text-anchor="middle" x="2269.9919" y="-579.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel1 -->
<g id="node62" class="node">
<title>Slide_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5814.9919" cy="-279" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="5814.9919" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel1</text>
</g>
<!-- Slide_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge71" class="edge">
<title>Slide_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5765.805,-264.0181C5722.3922,-251.6086 5657.148,-234.9281 5598.9919,-228 5222.6478,-183.1663 2564.509,-253.3579 2187.9919,-210 2181.4196,-209.2432 2174.5957,-208.1569 2167.8347,-206.8877"/>
<polygon fill="#000000" stroke="#000000" points="2168.5038,-203.4523 2158.0104,-204.9146 2167.1254,-210.3153 2168.5038,-203.4523"/>
<text text-anchor="middle" x="5755.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScDNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge72" class="edge">
<title>ScDNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5251.461,-261.5535C5230.7693,-249.5101 5201.2457,-234.5331 5172.9919,-228 5011.4187,-190.6397 2352.7324,-229.0336 2187.9919,-210 2181.4199,-209.2407 2174.5962,-208.1528 2167.8352,-206.8828"/>
<polygon fill="#000000" stroke="#000000" points="2168.5046,-203.4474 2158.0111,-204.9087 2167.1256,-210.3102 2168.5046,-203.4474"/>
<text text-anchor="middle" x="5288.9919" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel2&#45;&gt;ScRNA_seqLevel1 -->
<g id="edge63" class="edge">
<title>ScRNA_seqLevel2&#45;&gt;ScRNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M5649.8935,-347.9735C5635.6225,-335.1738 5616.286,-317.8308 5600.5732,-303.7379"/>
<polygon fill="#000000" stroke="#000000" points="5602.5141,-300.7771 5592.7328,-296.7057 5597.8402,-305.9882 5602.5141,-300.7771"/>
<text text-anchor="middle" x="5700.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel2&#45;&gt;Slide_seqLevel1 -->
<g id="edge65" class="edge">
<title>Slide_seqLevel2&#45;&gt;Slide_seqLevel1</title>
<path fill="none" stroke="#000000" d="M5859.3887,-347.9735C5851.5047,-335.7252 5840.9428,-319.3165 5832.0987,-305.5766"/>
<polygon fill="#000000" stroke="#000000" points="5834.9358,-303.5176 5826.5803,-297.0034 5829.0498,-307.3064 5834.9358,-303.5176"/>
<text text-anchor="middle" x="5919.9919" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
</g>
</svg>
</div>
