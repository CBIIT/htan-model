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
<svg width="6236pt" height="653pt"
 viewBox="0.00 0.00 6235.83 653.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 649)">
<title>Perl</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-649 6231.8276,-649 6231.8276,4 -4,4"/>
<!-- OvarianCancerTier3 -->
<g id="node1" class="node">
<title>OvarianCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="1397.8276" cy="-192" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="1397.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">OvarianCancerTier3</text>
</g>
<!-- Patient -->
<g id="node33" class="node">
<title>Patient</title>
<ellipse fill="none" stroke="#000000" cx="2883.8276" cy="-105" rx="44.393" ry="18"/>
<text text-anchor="middle" x="2883.8276" y="-101.3" font-family="Times,serif" font-size="14.00" fill="#000000">Patient</text>
</g>
<!-- OvarianCancerTier3&#45;&gt;Patient -->
<g id="edge51" class="edge">
<title>OvarianCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1445.5908,-175.8344C1483.6263,-163.7801 1538.4864,-148.2053 1587.8276,-141 1711.6936,-122.9118 2598.9064,-109.0759 2829.285,-105.7606"/>
<polygon fill="#000000" stroke="#000000" points="2829.4879,-109.2582 2839.4367,-105.6152 2829.3876,-102.2589 2829.4879,-109.2582"/>
<text text-anchor="middle" x="1661.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="node2" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="566.8276" cy="-279" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="566.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</text>
</g>
<!-- Biospecimen -->
<g id="node44" class="node">
<title>Biospecimen</title>
<ellipse fill="none" stroke="#000000" cx="2473.8276" cy="-192" rx="70.3881" ry="18"/>
<text text-anchor="middle" x="2473.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">Biospecimen</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge49" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M632.8067,-261.5698C681.5866,-249.5769 749.8452,-234.6554 810.8276,-228 1160.7724,-189.8081 2045.2401,-251.3352 2394.8276,-210 2401.1531,-209.2521 2407.7126,-208.2056 2414.2253,-206.9895"/>
<polygon fill="#000000" stroke="#000000" points="2415.2618,-210.3516 2424.3807,-204.9576 2413.8884,-203.4876 2415.2618,-210.3516"/>
<text text-anchor="middle" x="884.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel4 -->
<g id="node3" class="node">
<title>MassSpectrometryLevel4</title>
<ellipse fill="none" stroke="#000000" cx="3008.8276" cy="-540" rx="130.777" ry="18"/>
<text text-anchor="middle" x="3008.8276" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel4</text>
</g>
<!-- MassSpectrometryLevel3 -->
<g id="node24" class="node">
<title>MassSpectrometryLevel3</title>
<ellipse fill="none" stroke="#000000" cx="3008.8276" cy="-453" rx="130.777" ry="18"/>
<text text-anchor="middle" x="3008.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel3</text>
</g>
<!-- MassSpectrometryLevel4&#45;&gt;MassSpectrometryLevel3 -->
<g id="edge50" class="edge">
<title>MassSpectrometryLevel4&#45;&gt;MassSpectrometryLevel3</title>
<path fill="none" stroke="#000000" d="M3008.8276,-521.9735C3008.8276,-510.1918 3008.8276,-494.5607 3008.8276,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="3012.3277,-481.0033 3008.8276,-471.0034 3005.3277,-481.0034 3012.3277,-481.0033"/>
<text text-anchor="middle" x="3082.8276" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScDNA_seqLevel2 -->
<g id="node4" class="node">
<title>ScDNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1313.8276" cy="-366" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="1313.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScDNA_seqLevel2</text>
</g>
<!-- ScDNA_seqLevel1 -->
<g id="node10" class="node">
<title>ScDNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1313.8276" cy="-279" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="1313.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScDNA_seqLevel1</text>
</g>
<!-- ScDNA_seqLevel2&#45;&gt;ScDNA_seqLevel1 -->
<g id="edge48" class="edge">
<title>ScDNA_seqLevel2&#45;&gt;ScDNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M1313.8276,-347.9735C1313.8276,-336.1918 1313.8276,-320.5607 1313.8276,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1317.3277,-307.0033 1313.8276,-297.0034 1310.3277,-307.0034 1317.3277,-307.0033"/>
<text text-anchor="middle" x="1387.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- FollowUp -->
<g id="node5" class="node">
<title>FollowUp</title>
<ellipse fill="none" stroke="#000000" cx="2369.8276" cy="-18" rx="54.6905" ry="18"/>
<text text-anchor="middle" x="2369.8276" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">FollowUp</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="node6" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="356.8276" cy="-366" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="356.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel2&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="edge47" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel2&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M399.8309,-348.1843C432.9556,-334.4612 478.9055,-315.4249 514.2221,-300.7937"/>
<polygon fill="#000000" stroke="#000000" points="515.9827,-303.8528 523.8817,-296.7919 513.3035,-297.3858 515.9827,-303.8528"/>
<text text-anchor="middle" x="548.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- OtherAssay -->
<g id="node7" class="node">
<title>OtherAssay</title>
<ellipse fill="none" stroke="#000000" cx="902.8276" cy="-279" rx="65.7887" ry="18"/>
<text text-anchor="middle" x="902.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">OtherAssay</text>
</g>
<!-- OtherAssay&#45;&gt;Biospecimen -->
<g id="edge46" class="edge">
<title>OtherAssay&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M927.8574,-262.1224C947.3485,-250.0278 975.5836,-234.7327 1002.8276,-228 1152.9898,-190.8908 2241.2323,-228.2831 2394.8276,-210 2401.1525,-209.2471 2407.7116,-208.1974 2414.2241,-206.9794"/>
<polygon fill="#000000" stroke="#000000" points="2415.2614,-210.3413 2424.3793,-204.9455 2413.8867,-203.4776 2415.2614,-210.3413"/>
<text text-anchor="middle" x="1076.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel3 -->
<g id="node8" class="node">
<title>ElectronMicroscopyLevel3</title>
<ellipse fill="none" stroke="#000000" cx="3504.8276" cy="-453" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3504.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel3</text>
</g>
<!-- ElectronMicroscopyLevel2 -->
<g id="node37" class="node">
<title>ElectronMicroscopyLevel2</title>
<ellipse fill="none" stroke="#000000" cx="3504.8276" cy="-366" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3504.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel2</text>
</g>
<!-- ElectronMicroscopyLevel3&#45;&gt;ElectronMicroscopyLevel2 -->
<g id="edge44" class="edge">
<title>ElectronMicroscopyLevel3&#45;&gt;ElectronMicroscopyLevel2</title>
<path fill="none" stroke="#000000" d="M3504.8276,-434.9735C3504.8276,-423.1918 3504.8276,-407.5607 3504.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="3508.3277,-394.0033 3504.8276,-384.0034 3501.3277,-394.0034 3508.3277,-394.0033"/>
<text text-anchor="middle" x="3578.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel1 -->
<g id="node9" class="node">
<title>BulkRNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1092.8276" cy="-279" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="1092.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel1</text>
</g>
<!-- BulkRNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge45" class="edge">
<title>BulkRNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1119.6663,-261.3775C1139.519,-249.4166 1167.7073,-234.6173 1194.8276,-228 1324.3753,-196.3904 2262.4304,-225.8987 2394.8276,-210 2401.1517,-209.2406 2407.7103,-208.1866 2414.2225,-206.9661"/>
<polygon fill="#000000" stroke="#000000" points="2415.2609,-210.3277 2424.3774,-204.9295 2413.8844,-203.4643 2415.2609,-210.3277"/>
<text text-anchor="middle" x="1268.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScDNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge43" class="edge">
<title>ScDNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1327.2691,-261.0136C1337.264,-249.2126 1352.0358,-234.7577 1368.8276,-228 1421.7142,-206.7161 2338.2341,-216.869 2394.8276,-210 2401.1508,-209.2325 2407.7087,-208.1734 2414.2205,-206.9498"/>
<polygon fill="#000000" stroke="#000000" points="2415.2603,-210.3109 2424.375,-204.9099 2413.8815,-203.4481 2415.2603,-210.3109"/>
<text text-anchor="middle" x="1442.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel1 -->
<g id="node11" class="node">
<title>HI_C_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="1515.8276" cy="-279" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="1515.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel1</text>
</g>
<!-- HI_C_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge42" class="edge">
<title>HI_C_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1516.0527,-260.9131C1517.2464,-249.541 1520.8566,-235.6239 1530.8276,-228 1568.9667,-198.8383 2347.1765,-215.8631 2394.8276,-210 2401.1495,-209.2221 2407.7066,-208.1563 2414.218,-206.9287"/>
<polygon fill="#000000" stroke="#000000" points="2415.2594,-210.2893 2424.3719,-204.8846 2413.8778,-203.427 2415.2594,-210.2893"/>
<text text-anchor="middle" x="1604.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel3 -->
<g id="node12" class="node">
<title>RPPALevel3</title>
<ellipse fill="none" stroke="#000000" cx="1688.8276" cy="-279" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="1688.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel3</text>
</g>
<!-- RPPALevel3&#45;&gt;Biospecimen -->
<g id="edge41" class="edge">
<title>RPPALevel3&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1683.0853,-260.5855C1680.9242,-249.6668 1680.6693,-236.369 1688.8276,-228 1716.215,-199.9054 2355.8975,-214.8821 2394.8276,-210 2401.1477,-209.2074 2407.7036,-208.132 2414.2142,-206.8987"/>
<polygon fill="#000000" stroke="#000000" points="2415.2581,-210.2587 2424.3675,-204.8486 2413.8725,-203.3972 2415.2581,-210.2587"/>
<text text-anchor="middle" x="1762.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="node13" class="node">
<title>NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<ellipse fill="none" stroke="#000000" cx="4553.8276" cy="-279" rx="294.3478" ry="18"/>
<text text-anchor="middle" x="4553.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</text>
</g>
<!-- Demographics -->
<g id="node14" class="node">
<title>Demographics</title>
<ellipse fill="none" stroke="#000000" cx="2539.8276" cy="-18" rx="77.9862" ry="18"/>
<text text-anchor="middle" x="2539.8276" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Demographics</text>
</g>
<!-- HI_C_seqLevel3 -->
<g id="node15" class="node">
<title>HI_C_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="1515.8276" cy="-453" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="1515.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel3</text>
</g>
<!-- HI_C_seqLevel2 -->
<g id="node28" class="node">
<title>HI_C_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1515.8276" cy="-366" rx="87.1846" ry="18"/>
<text text-anchor="middle" x="1515.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">HI_C_seqLevel2</text>
</g>
<!-- HI_C_seqLevel3&#45;&gt;HI_C_seqLevel2 -->
<g id="edge40" class="edge">
<title>HI_C_seqLevel3&#45;&gt;HI_C_seqLevel2</title>
<path fill="none" stroke="#000000" d="M1515.8276,-434.9735C1515.8276,-423.1918 1515.8276,-407.5607 1515.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="1519.3277,-394.0033 1515.8276,-384.0034 1512.3277,-394.0034 1519.3277,-394.0033"/>
<text text-anchor="middle" x="1589.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel2 -->
<g id="node16" class="node">
<title>Slide_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="3744.8276" cy="-366" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="3744.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel2</text>
</g>
<!-- Slide_seqLevel1 -->
<g id="node61" class="node">
<title>Slide_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="3744.8276" cy="-279" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="3744.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel1</text>
</g>
<!-- Slide_seqLevel2&#45;&gt;Slide_seqLevel1 -->
<g id="edge39" class="edge">
<title>Slide_seqLevel2&#45;&gt;Slide_seqLevel1</title>
<path fill="none" stroke="#000000" d="M3744.8276,-347.9735C3744.8276,-336.1918 3744.8276,-320.5607 3744.8276,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="3748.3277,-307.0033 3744.8276,-297.0034 3741.3277,-307.0034 3748.3277,-307.0033"/>
<text text-anchor="middle" x="3818.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MolecularTest -->
<g id="node17" class="node">
<title>MolecularTest</title>
<ellipse fill="none" stroke="#000000" cx="2712.8276" cy="-18" rx="77.1866" ry="18"/>
<text text-anchor="middle" x="2712.8276" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">MolecularTest</text>
</g>
<!-- HTANRPPAAntibodyTable -->
<g id="node18" class="node">
<title>HTANRPPAAntibodyTable</title>
<ellipse fill="none" stroke="#000000" cx="2727.8276" cy="-366" rx="132.6765" ry="18"/>
<text text-anchor="middle" x="2727.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">HTANRPPAAntibodyTable</text>
</g>
<!-- RPPALevel2 -->
<g id="node36" class="node">
<title>RPPALevel2</title>
<ellipse fill="none" stroke="#000000" cx="2562.8276" cy="-279" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="2562.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel2</text>
</g>
<!-- HTANRPPAAntibodyTable&#45;&gt;RPPALevel2 -->
<g id="edge83" class="edge">
<title>HTANRPPAAntibodyTable&#45;&gt;RPPALevel2</title>
<path fill="none" stroke="#000000" d="M2718.8209,-348.002C2712.427,-336.9616 2702.8532,-323.3811 2690.8276,-315 2684.7609,-310.7719 2652.7008,-301.7576 2622.1874,-293.8075"/>
<polygon fill="#000000" stroke="#000000" points="2622.9273,-290.3838 2612.3697,-291.2711 2621.1763,-297.1613 2622.9273,-290.3838"/>
<text text-anchor="middle" x="2778.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BreastCancerTier3 -->
<g id="node19" class="node">
<title>BreastCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="1622.8276" cy="-192" rx="100.1823" ry="18"/>
<text text-anchor="middle" x="1622.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">BreastCancerTier3</text>
</g>
<!-- BreastCancerTier3&#45;&gt;Patient -->
<g id="edge84" class="edge">
<title>BreastCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1668.7922,-175.8974C1705.4049,-163.8779 1758.234,-148.3191 1805.8276,-141 1907.1902,-125.4122 2624.4609,-110.1405 2829.3168,-106.0584"/>
<polygon fill="#000000" stroke="#000000" points="2829.603,-109.5535 2839.5316,-105.8557 2829.4641,-102.5549 2829.603,-109.5535"/>
<text text-anchor="middle" x="1879.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- FamilyHistory -->
<g id="node20" class="node">
<title>FamilyHistory</title>
<ellipse fill="none" stroke="#000000" cx="2885.8276" cy="-18" rx="77.1866" ry="18"/>
<text text-anchor="middle" x="2885.8276" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">FamilyHistory</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3 -->
<g id="node21" class="node">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3</title>
<ellipse fill="none" stroke="#000000" cx="5090.8276" cy="-453" rx="258.0542" ry="18"/>
<text text-anchor="middle" x="5090.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPSpatialTranscriptomicsLevel3</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="edge80" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M4884.0524,-442.2227C4773.9166,-432.8658 4652.2012,-415.6012 4607.8276,-384 4582.1139,-365.6877 4567.7956,-331.4103 4560.4678,-307.0026"/>
<polygon fill="#000000" stroke="#000000" points="4563.7983,-305.9153 4557.7425,-297.2217 4557.0552,-307.7942 4563.7983,-305.9153"/>
<text text-anchor="middle" x="4681.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1 -->
<g id="node25" class="node">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5022.8276" cy="-366" rx="258.0542" ry="18"/>
<text text-anchor="middle" x="5022.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPSpatialTranscriptomicsLevel1 -->
<g id="edge79" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPSpatialTranscriptomicsLevel1</title>
<path fill="none" stroke="#000000" d="M5076.7379,-434.9735C5067.0733,-422.6085 5054.0947,-406.0036 5043.2938,-392.1847"/>
<polygon fill="#000000" stroke="#000000" points="5045.815,-389.7269 5036.8992,-384.0034 5040.2998,-394.0376 5045.815,-389.7269"/>
<text text-anchor="middle" x="5134.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel2 -->
<g id="node46" class="node">
<title>ImagingLevel2</title>
<ellipse fill="none" stroke="#000000" cx="5645.8276" cy="-366" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="5645.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel2</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;ImagingLevel2 -->
<g id="edge78" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M5215.067,-437.1682C5257.5706,-431.3529 5305.3535,-424.3739 5348.8276,-417 5382.3423,-411.3153 5390.3777,-408.055 5423.8276,-402 5472.0238,-393.2756 5526.2915,-384.4573 5569.108,-377.7319"/>
<polygon fill="#000000" stroke="#000000" points="5569.8374,-381.1604 5579.1758,-376.1559 5568.7548,-374.2447 5569.8374,-381.1604"/>
<text text-anchor="middle" x="5497.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="node60" class="node">
<title>NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<ellipse fill="none" stroke="#000000" cx="5344.8276" cy="-279" rx="295.1477" ry="18"/>
<text text-anchor="middle" x="5344.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="edge77" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel3&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M5185.906,-436.2347C5221.7794,-426.0284 5260.8739,-409.7694 5289.8276,-384 5313.1269,-363.2631 5328.1167,-330.274 5336.469,-306.8104"/>
<polygon fill="#000000" stroke="#000000" points="5339.8679,-307.6843 5339.7464,-297.0902 5333.2348,-305.4478 5339.8679,-307.6843"/>
<text text-anchor="middle" x="5390.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel3 -->
<g id="node22" class="node">
<title>BulkMethylation_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="2128.8276" cy="-453" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="2128.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel3</text>
</g>
<!-- BulkMethylation_seqLevel2 -->
<g id="node26" class="node">
<title>BulkMethylation_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2042.8276" cy="-366" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="2042.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel2</text>
</g>
<!-- BulkMethylation_seqLevel3&#45;&gt;BulkMethylation_seqLevel2 -->
<g id="edge81" class="edge">
<title>BulkMethylation_seqLevel3&#45;&gt;BulkMethylation_seqLevel2</title>
<path fill="none" stroke="#000000" d="M2075.1178,-436.1554C2066.2276,-431.2368 2057.9329,-424.9637 2051.8276,-417 2046.883,-410.5503 2044.3081,-402.297 2043.0459,-394.3178"/>
<polygon fill="#000000" stroke="#000000" points="2046.5095,-393.7735 2042.054,-384.1611 2039.5427,-394.454 2046.5095,-393.7735"/>
<text text-anchor="middle" x="2125.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel3&#45;&gt;Biospecimen -->
<g id="edge82" class="edge">
<title>BulkMethylation_seqLevel3&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2178.4587,-435.996C2186.7518,-431.0782 2194.4079,-424.8462 2199.8276,-417 2225.7414,-379.4835 2184.6053,-352.3016 2210.8276,-315 2221.3445,-300.0396 2232.7924,-307.4097 2247.8276,-297 2266.955,-283.757 2266.0559,-273.2604 2285.8276,-261 2325.2931,-236.5275 2374.7526,-218.809 2413.0349,-207.4585"/>
<polygon fill="#000000" stroke="#000000" points="2414.3834,-210.7118 2423.0149,-204.5678 2412.4359,-203.9881 2414.3834,-210.7118"/>
<text text-anchor="middle" x="2284.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel4 -->
<g id="node23" class="node">
<title>RPPALevel4</title>
<ellipse fill="none" stroke="#000000" cx="2509.8276" cy="-366" rx="67.6881" ry="18"/>
<text text-anchor="middle" x="2509.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">RPPALevel4</text>
</g>
<!-- RPPALevel4&#45;&gt;RPPALevel2 -->
<g id="edge76" class="edge">
<title>RPPALevel4&#45;&gt;RPPALevel2</title>
<path fill="none" stroke="#000000" d="M2520.8092,-347.9735C2528.2709,-335.7252 2538.2669,-319.3165 2546.6373,-305.5766"/>
<polygon fill="#000000" stroke="#000000" points="2549.6464,-307.3644 2551.86,-297.0034 2543.6683,-303.7225 2549.6464,-307.3644"/>
<text text-anchor="middle" x="2612.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel2 -->
<g id="node69" class="node">
<title>MassSpectrometryLevel2</title>
<ellipse fill="none" stroke="#000000" cx="3008.8276" cy="-366" rx="130.777" ry="18"/>
<text text-anchor="middle" x="3008.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel2</text>
</g>
<!-- MassSpectrometryLevel3&#45;&gt;MassSpectrometryLevel2 -->
<g id="edge75" class="edge">
<title>MassSpectrometryLevel3&#45;&gt;MassSpectrometryLevel2</title>
<path fill="none" stroke="#000000" d="M3008.8276,-434.9735C3008.8276,-423.1918 3008.8276,-407.5607 3008.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="3012.3277,-394.0033 3008.8276,-384.0034 3005.3277,-394.0034 3012.3277,-394.0033"/>
<text text-anchor="middle" x="3082.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata -->
<g id="edge72" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIRCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M4861.077,-351.9439C4815.7559,-346.5756 4766.6387,-339.4052 4721.8276,-330 4685.3312,-322.3399 4645.3483,-310.3534 4613.5469,-299.9251"/>
<polygon fill="#000000" stroke="#000000" points="4614.5465,-296.5692 4603.9531,-296.7453 4612.3442,-303.2138 4614.5465,-296.5692"/>
<text text-anchor="middle" x="4795.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;Biospecimen -->
<g id="edge74" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M4982.038,-348.2106C4955.4555,-335.7086 4920.6665,-317.5839 4892.8276,-297 4874.6334,-283.5474 4877.5122,-270.1732 4856.8276,-261 4721.1661,-200.8372 4338.1633,-232.4838 4189.8276,-228 4008.1218,-222.5075 2734.3913,-231.0688 2553.8276,-210 2547.1773,-209.224 2540.2704,-208.1256 2533.4256,-206.8495"/>
<polygon fill="#000000" stroke="#000000" points="2533.9698,-203.3892 2523.4789,-204.8695 2532.6031,-210.2545 2533.9698,-203.3892"/>
<text text-anchor="middle" x="4966.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata -->
<g id="edge73" class="edge">
<title>NanoStringGeoMxDSPSpatialTranscriptomicsLevel1&#45;&gt;NanoStringGeoMxDSPROIDCCSegmentAnnotationMetadata</title>
<path fill="none" stroke="#000000" d="M5070.3323,-348.1969C5099.6083,-337.6397 5138.0721,-324.5079 5172.8276,-315 5195.3575,-308.8366 5219.7958,-303.1398 5242.9856,-298.1818"/>
<polygon fill="#000000" stroke="#000000" points="5243.7765,-301.5921 5252.8385,-296.103 5242.3313,-294.7429 5243.7765,-301.5921"/>
<text text-anchor="middle" x="5246.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel1 -->
<g id="node38" class="node">
<title>BulkMethylation_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2098.8276" cy="-279" rx="140.2752" ry="18"/>
<text text-anchor="middle" x="2098.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkMethylation_seqLevel1</text>
</g>
<!-- BulkMethylation_seqLevel2&#45;&gt;BulkMethylation_seqLevel1 -->
<g id="edge71" class="edge">
<title>BulkMethylation_seqLevel2&#45;&gt;BulkMethylation_seqLevel1</title>
<path fill="none" stroke="#000000" d="M2039.2113,-347.9387C2038.0892,-337.6683 2038.3392,-324.9183 2043.8276,-315 2046.3192,-310.4972 2049.6396,-306.4638 2053.4195,-302.874"/>
<polygon fill="#000000" stroke="#000000" points="2055.6567,-305.5656 2061.1576,-296.5107 2051.2106,-300.1589 2055.6567,-305.5656"/>
<text text-anchor="middle" x="2117.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel2&#45;&gt;Biospecimen -->
<g id="edge70" class="edge">
<title>BulkMethylation_seqLevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M1936.2369,-354.2389C1851.7266,-340.765 1755.0029,-313.4145 1801.8276,-261 1845.8862,-211.6817 2329.3599,-219.3512 2394.8276,-210 2401.0418,-209.1124 2407.4901,-207.9873 2413.9019,-206.7344"/>
<polygon fill="#000000" stroke="#000000" points="2414.819,-210.1191 2423.9089,-204.6763 2413.4088,-203.2627 2414.819,-210.1191"/>
<text text-anchor="middle" x="1875.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScmC_seqLevel1 -->
<g id="node27" class="node">
<title>ScmC_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2385.8276" cy="-279" rx="90.9839" ry="18"/>
<text text-anchor="middle" x="2385.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScmC_seqLevel1</text>
</g>
<!-- ScmC_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge68" class="edge">
<title>ScmC_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2382.8911,-260.9165C2382.1731,-250.3878 2383.0995,-237.3828 2389.8276,-228 2395.6524,-219.8769 2403.6975,-213.5716 2412.5174,-208.6814"/>
<polygon fill="#000000" stroke="#000000" points="2414.1098,-211.7987 2421.542,-204.248 2411.0233,-205.5159 2414.1098,-211.7987"/>
<text text-anchor="middle" x="2463.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- HI_C_seqLevel2&#45;&gt;HI_C_seqLevel1 -->
<g id="edge69" class="edge">
<title>HI_C_seqLevel2&#45;&gt;HI_C_seqLevel1</title>
<path fill="none" stroke="#000000" d="M1515.8276,-347.9735C1515.8276,-336.1918 1515.8276,-320.5607 1515.8276,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1519.3277,-307.0033 1515.8276,-297.0034 1512.3277,-307.0034 1519.3277,-307.0033"/>
<text text-anchor="middle" x="1589.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Diagnosis -->
<g id="node29" class="node">
<title>Diagnosis</title>
<ellipse fill="none" stroke="#000000" cx="3054.8276" cy="-18" rx="55.7903" ry="18"/>
<text text-anchor="middle" x="3054.8276" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Diagnosis</text>
</g>
<!-- ImagingLevel4 -->
<g id="node30" class="node">
<title>ImagingLevel4</title>
<ellipse fill="none" stroke="#000000" cx="6092.8276" cy="-453" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="6092.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel4</text>
</g>
<!-- ImagingLevel3Channels -->
<g id="node51" class="node">
<title>ImagingLevel3Channels</title>
<ellipse fill="none" stroke="#000000" cx="6007.8276" cy="-366" rx="124.2781" ry="18"/>
<text text-anchor="middle" x="6007.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Channels</text>
</g>
<!-- ImagingLevel4&#45;&gt;ImagingLevel3Channels -->
<g id="edge67" class="edge">
<title>ImagingLevel4&#45;&gt;ImagingLevel3Channels</title>
<path fill="none" stroke="#000000" d="M6088.157,-434.8897C6084.7248,-424.3514 6079.1821,-411.3459 6070.8276,-402 6066.475,-397.131 6061.3015,-392.7576 6055.8182,-388.8788"/>
<polygon fill="#000000" stroke="#000000" points="6057.3181,-385.6807 6047.02,-383.1905 6053.5175,-391.5591 6057.3181,-385.6807"/>
<text text-anchor="middle" x="6153.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Exposure -->
<g id="node31" class="node">
<title>Exposure</title>
<ellipse fill="none" stroke="#000000" cx="3225.8276" cy="-18" rx="54.6905" ry="18"/>
<text text-anchor="middle" x="3225.8276" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Exposure</text>
</g>
<!-- Slide_seqLevel3 -->
<g id="node32" class="node">
<title>Slide_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="3744.8276" cy="-453" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="3744.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">Slide_seqLevel3</text>
</g>
<!-- Slide_seqLevel3&#45;&gt;Slide_seqLevel2 -->
<g id="edge66" class="edge">
<title>Slide_seqLevel3&#45;&gt;Slide_seqLevel2</title>
<path fill="none" stroke="#000000" d="M3744.8276,-434.9735C3744.8276,-423.1918 3744.8276,-407.5607 3744.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="3748.3277,-394.0033 3744.8276,-384.0034 3741.3277,-394.0034 3748.3277,-394.0033"/>
<text text-anchor="middle" x="3818.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;FollowUp -->
<g id="edge62" class="edge">
<title>Patient&#45;&gt;FollowUp</title>
<path fill="none" stroke="#000000" d="M2839.6775,-103.9591C2727.6881,-101.0024 2438.7935,-91.2839 2401.8276,-69 2392.7252,-63.5129 2385.8053,-54.339 2380.7701,-45.2726"/>
<polygon fill="#000000" stroke="#000000" points="2383.7648,-43.4328 2376.1927,-36.0224 2377.4909,-46.5374 2383.7648,-43.4328"/>
<text text-anchor="middle" x="2475.8276" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Demographics -->
<g id="edge63" class="edge">
<title>Patient&#45;&gt;Demographics</title>
<path fill="none" stroke="#000000" d="M2840.012,-102.192C2758.7725,-96.6664 2590.9876,-83.6385 2568.8276,-69 2560.2492,-63.3333 2553.9272,-54.2067 2549.4157,-45.2294"/>
<polygon fill="#000000" stroke="#000000" points="2552.6095,-43.7975 2545.3511,-36.0796 2546.2123,-46.6394 2552.6095,-43.7975"/>
<text text-anchor="middle" x="2642.8276" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;MolecularTest -->
<g id="edge59" class="edge">
<title>Patient&#45;&gt;MolecularTest</title>
<path fill="none" stroke="#000000" d="M2841.4879,-99.5023C2802.3657,-93.636 2747.9374,-83.2256 2731.8276,-69 2725.0062,-62.9764 2720.6282,-54.2666 2717.8206,-45.7444"/>
<polygon fill="#000000" stroke="#000000" points="2721.1757,-44.7429 2715.1938,-35.9983 2714.4169,-46.5647 2721.1757,-44.7429"/>
<text text-anchor="middle" x="2805.8276" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;FamilyHistory -->
<g id="edge64" class="edge">
<title>Patient&#45;&gt;FamilyHistory</title>
<path fill="none" stroke="#000000" d="M2884.1524,-86.5864C2884.3326,-76.8901 2884.5717,-64.8011 2884.8276,-54 2884.885,-51.574 2884.9481,-49.0561 2885.0137,-46.5299"/>
<polygon fill="#000000" stroke="#000000" points="2888.5182,-46.4044 2885.2899,-36.3134 2881.5208,-46.2151 2888.5182,-46.4044"/>
<text text-anchor="middle" x="2958.8276" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Diagnosis -->
<g id="edge61" class="edge">
<title>Patient&#45;&gt;Diagnosis</title>
<path fill="none" stroke="#000000" d="M2925.9115,-99.1109C2964.0974,-93.0197 3016.8027,-82.5059 3032.8276,-69 3039.929,-63.0148 3044.801,-54.3145 3048.1159,-45.7892"/>
<polygon fill="#000000" stroke="#000000" points="3051.5246,-46.6278 3051.3322,-36.0347 3044.8767,-44.4357 3051.5246,-46.6278"/>
<text text-anchor="middle" x="3117.8276" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Patient&#45;&gt;Exposure -->
<g id="edge65" class="edge">
<title>Patient&#45;&gt;Exposure</title>
<path fill="none" stroke="#000000" d="M2927.5205,-102.1179C3008.0722,-96.4908 3173.8063,-83.3326 3195.8276,-69 3204.5178,-63.3439 3211.019,-54.2195 3215.7064,-45.2411"/>
<polygon fill="#000000" stroke="#000000" points="3218.9187,-46.6335 3219.9503,-36.089 3212.5682,-43.6887 3218.9187,-46.6335"/>
<text text-anchor="middle" x="3283.8276" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Therapy -->
<g id="node68" class="node">
<title>Therapy</title>
<ellipse fill="none" stroke="#000000" cx="3396.8276" cy="-18" rx="49.2915" ry="18"/>
<text text-anchor="middle" x="3396.8276" y="-14.3" font-family="Times,serif" font-size="14.00" fill="#000000">Therapy</text>
</g>
<!-- Patient&#45;&gt;Therapy -->
<g id="edge60" class="edge">
<title>Patient&#45;&gt;Therapy</title>
<path fill="none" stroke="#000000" d="M2927.9654,-103.8398C3039.1932,-100.6122 3324.7721,-90.3277 3361.8276,-69 3371.4605,-63.4557 3379.0252,-54.0582 3384.6196,-44.8295"/>
<polygon fill="#000000" stroke="#000000" points="3387.8276,-46.2581 3389.5607,-35.8059 3381.6879,-42.896 3387.8276,-46.2581"/>
<text text-anchor="middle" x="3451.8276" y="-57.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel3 -->
<g id="node34" class="node">
<title>ScRNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="3253.8276" cy="-453" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="3253.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel3</text>
</g>
<!-- ScRNA_seqLevel2 -->
<g id="node75" class="node">
<title>ScRNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="3253.8276" cy="-366" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="3253.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel2</text>
</g>
<!-- ScRNA_seqLevel3&#45;&gt;ScRNA_seqLevel2 -->
<g id="edge58" class="edge">
<title>ScRNA_seqLevel3&#45;&gt;ScRNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M3253.8276,-434.9735C3253.8276,-423.1918 3253.8276,-407.5607 3253.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="3257.3277,-394.0033 3253.8276,-384.0034 3250.3277,-394.0034 3257.3277,-394.0033"/>
<text text-anchor="middle" x="3327.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- PancreaticCancerTier3 -->
<g id="node35" class="node">
<title>PancreaticCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="1859.8276" cy="-192" rx="118.8789" ry="18"/>
<text text-anchor="middle" x="1859.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">PancreaticCancerTier3</text>
</g>
<!-- PancreaticCancerTier3&#45;&gt;Patient -->
<g id="edge57" class="edge">
<title>PancreaticCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1900.2422,-175.0622C1930.6228,-163.1894 1973.5841,-148.2031 2012.8276,-141 2170.504,-112.0585 2663.6866,-106.3639 2829.1113,-105.2605"/>
<polygon fill="#000000" stroke="#000000" points="2829.549,-108.7579 2839.5265,-105.1943 2829.5044,-101.758 2829.549,-108.7579"/>
<text text-anchor="middle" x="2086.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- RPPALevel2&#45;&gt;Biospecimen -->
<g id="edge56" class="edge">
<title>RPPALevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2557.0189,-260.8689C2552.941,-250.3233 2546.6318,-237.3173 2537.8276,-228 2532.3484,-222.2015 2525.7238,-217.0868 2518.841,-212.6679"/>
<polygon fill="#000000" stroke="#000000" points="2520.4361,-209.5445 2510.0516,-207.4438 2516.8596,-215.5618 2520.4361,-209.5445"/>
<text text-anchor="middle" x="2621.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel1 -->
<g id="node59" class="node">
<title>ElectronMicroscopyLevel1</title>
<ellipse fill="none" stroke="#000000" cx="3504.8276" cy="-279" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3504.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel1</text>
</g>
<!-- ElectronMicroscopyLevel2&#45;&gt;ElectronMicroscopyLevel1 -->
<g id="edge55" class="edge">
<title>ElectronMicroscopyLevel2&#45;&gt;ElectronMicroscopyLevel1</title>
<path fill="none" stroke="#000000" d="M3504.8276,-347.9735C3504.8276,-336.1918 3504.8276,-320.5607 3504.8276,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="3508.3277,-307.0033 3504.8276,-297.0034 3501.3277,-307.0034 3508.3277,-307.0033"/>
<text text-anchor="middle" x="3578.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkMethylation_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge54" class="edge">
<title>BulkMethylation_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2095.7049,-260.8864C2094.9134,-249.7998 2096.1506,-236.2114 2104.8276,-228 2128.2764,-205.8093 2362.8729,-214.6011 2394.8276,-210 2401.0408,-209.1054 2407.4884,-207.9757 2413.8999,-206.7201"/>
<polygon fill="#000000" stroke="#000000" points="2414.8181,-210.1045 2423.9064,-204.659 2413.4059,-203.2484 2414.8181,-210.1045"/>
<text text-anchor="middle" x="2178.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SarcomaTier3 -->
<g id="node39" class="node">
<title>SarcomaTier3</title>
<ellipse fill="none" stroke="#000000" cx="2073.8276" cy="-192" rx="76.8869" ry="18"/>
<text text-anchor="middle" x="2073.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">SarcomaTier3</text>
</g>
<!-- SarcomaTier3&#45;&gt;Patient -->
<g id="edge53" class="edge">
<title>SarcomaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2109.4766,-175.915C2137.7061,-163.9895 2178.4691,-148.5466 2215.8276,-141 2332.603,-117.4107 2691.2182,-108.5097 2829.0625,-105.9046"/>
<polygon fill="#000000" stroke="#000000" points="2829.4447,-109.3982 2839.3782,-105.7137 2829.3151,-102.3994 2829.4447,-109.3982"/>
<text text-anchor="middle" x="2289.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ProstateCancerTier3 -->
<g id="node40" class="node">
<title>ProstateCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="2276.8276" cy="-192" rx="108.5808" ry="18"/>
<text text-anchor="middle" x="2276.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">ProstateCancerTier3</text>
</g>
<!-- ProstateCancerTier3&#45;&gt;Patient -->
<g id="edge52" class="edge">
<title>ProstateCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2315.7502,-175.0684C2344.2773,-163.4419 2384.2458,-148.7585 2420.8276,-141 2497.5377,-124.7308 2724.9966,-112.4004 2829.8196,-107.4165"/>
<polygon fill="#000000" stroke="#000000" points="2830.049,-110.9097 2839.8733,-106.9432 2829.7197,-103.9174 2830.049,-110.9097"/>
<text text-anchor="middle" x="2494.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel4 -->
<g id="node41" class="node">
<title>ScATAC_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="4140.8276" cy="-540" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="4140.8276" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel4</text>
</g>
<!-- ScATAC_seqLevel3 -->
<g id="node54" class="node">
<title>ScATAC_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="4140.8276" cy="-453" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="4140.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel3</text>
</g>
<!-- ScATAC_seqLevel4&#45;&gt;ScATAC_seqLevel3 -->
<g id="edge16" class="edge">
<title>ScATAC_seqLevel4&#45;&gt;ScATAC_seqLevel3</title>
<path fill="none" stroke="#000000" d="M4140.8276,-521.9735C4140.8276,-510.1918 4140.8276,-494.5607 4140.8276,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="4144.3277,-481.0033 4140.8276,-471.0034 4137.3277,-481.0034 4144.3277,-481.0033"/>
<text text-anchor="middle" x="4214.8276" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel1 -->
<g id="node42" class="node">
<title>MassSpectrometryLevel1</title>
<ellipse fill="none" stroke="#000000" cx="2778.8276" cy="-279" rx="130.777" ry="18"/>
<text text-anchor="middle" x="2778.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">MassSpectrometryLevel1</text>
</g>
<!-- MassSpectrometryLevel1&#45;&gt;Biospecimen -->
<g id="edge15" class="edge">
<title>MassSpectrometryLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2757.1159,-261.1286C2741.9991,-249.6959 2720.8524,-235.6261 2699.8276,-228 2638.3656,-205.7065 2618.2431,-221.1895 2553.8276,-210 2547.7525,-208.9447 2541.4431,-207.7313 2535.1526,-206.4434"/>
<polygon fill="#000000" stroke="#000000" points="2535.8264,-203.0086 2525.3194,-204.3703 2534.3823,-209.858 2535.8264,-203.0086"/>
<text text-anchor="middle" x="2803.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3 -->
<g id="node43" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="252.8276" cy="-540" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="252.8276" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="edge14" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M246.005,-521.991C238.8718,-499.9822 230.6496,-462.3063 245.8276,-435 257.3029,-414.3549 277.799,-399.0907 298.0824,-388.245"/>
<polygon fill="#000000" stroke="#000000" points="299.6964,-391.3509 307.0433,-383.7172 296.5395,-385.1032 299.6964,-391.3509"/>
<text text-anchor="middle" x="319.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles -->
<g id="node62" class="node">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</title>
<ellipse fill="none" stroke="#000000" cx="645.8276" cy="-453" rx="243.1569" ry="18"/>
<text text-anchor="middle" x="645.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_AuxiliaryFiles -->
<g id="edge13" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel3&#45;&gt;_10xVisiumSpatialTranscriptomics_AuxiliaryFiles</title>
<path fill="none" stroke="#000000" d="M330.4717,-522.8116C396.247,-508.2507 490.4825,-487.3894 558.7954,-472.2667"/>
<polygon fill="#000000" stroke="#000000" points="559.6727,-475.6573 568.6798,-470.0785 558.1596,-468.8227 559.6727,-475.6573"/>
<text text-anchor="middle" x="547.8276" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Biospecimen&#45;&gt;Patient -->
<g id="edge12" class="edge">
<title>Biospecimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2511.8192,-176.7224C2541.5787,-165.314 2584.2577,-150.1703 2622.8276,-141 2693.5424,-124.187 2777.032,-114.3757 2830.1904,-109.3519"/>
<polygon fill="#000000" stroke="#000000" points="2830.7684,-112.8135 2840.4049,-108.4103 2830.1258,-105.8431 2830.7684,-112.8135"/>
<text text-anchor="middle" x="2696.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel2 -->
<g id="node45" class="node">
<title>ScATAC_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="4140.8276" cy="-366" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="4140.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel2</text>
</g>
<!-- ScATAC_seqLevel1 -->
<g id="node65" class="node">
<title>ScATAC_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="4140.8276" cy="-279" rx="100.9827" ry="18"/>
<text text-anchor="middle" x="4140.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScATAC_seqLevel1</text>
</g>
<!-- ScATAC_seqLevel2&#45;&gt;ScATAC_seqLevel1 -->
<g id="edge11" class="edge">
<title>ScATAC_seqLevel2&#45;&gt;ScATAC_seqLevel1</title>
<path fill="none" stroke="#000000" d="M4140.8276,-347.9735C4140.8276,-336.1918 4140.8276,-320.5607 4140.8276,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="4144.3277,-307.0033 4140.8276,-297.0034 4137.3277,-307.0034 4144.3277,-307.0033"/>
<text text-anchor="middle" x="4214.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel1 -->
<g id="node74" class="node">
<title>ImagingLevel1</title>
<ellipse fill="none" stroke="#000000" cx="5738.8276" cy="-279" rx="80.6858" ry="18"/>
<text text-anchor="middle" x="5738.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel1</text>
</g>
<!-- ImagingLevel2&#45;&gt;ImagingLevel1 -->
<g id="edge10" class="edge">
<title>ImagingLevel2&#45;&gt;ImagingLevel1</title>
<path fill="none" stroke="#000000" d="M5664.6475,-348.3943C5678.3875,-335.5407 5697.1971,-317.9446 5712.4372,-303.6878"/>
<polygon fill="#000000" stroke="#000000" points="5715.1239,-305.9671 5720.0356,-296.5796 5710.3418,-300.8552 5715.1239,-305.9671"/>
<text text-anchor="middle" x="5771.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel3 -->
<g id="node47" class="node">
<title>BulkWESLevel3</title>
<ellipse fill="none" stroke="#000000" cx="3935.8276" cy="-453" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="3935.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel3</text>
</g>
<!-- BulkWESLevel2 -->
<g id="node57" class="node">
<title>BulkWESLevel2</title>
<ellipse fill="none" stroke="#000000" cx="3935.8276" cy="-366" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="3935.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel2</text>
</g>
<!-- BulkWESLevel3&#45;&gt;BulkWESLevel2 -->
<g id="edge9" class="edge">
<title>BulkWESLevel3&#45;&gt;BulkWESLevel2</title>
<path fill="none" stroke="#000000" d="M3935.8276,-434.9735C3935.8276,-423.1918 3935.8276,-407.5607 3935.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="3939.3277,-394.0033 3935.8276,-384.0034 3932.3277,-394.0034 3939.3277,-394.0033"/>
<text text-anchor="middle" x="4009.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- AcuteLymphoblasticLeukemiaTier3 -->
<g id="node48" class="node">
<title>AcuteLymphoblasticLeukemiaTier3</title>
<ellipse fill="none" stroke="#000000" cx="2739.8276" cy="-192" rx="177.3685" ry="18"/>
<text text-anchor="middle" x="2739.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">AcuteLymphoblasticLeukemiaTier3</text>
</g>
<!-- AcuteLymphoblasticLeukemiaTier3&#45;&gt;Patient -->
<g id="edge8" class="edge">
<title>AcuteLymphoblasticLeukemiaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2756.2991,-173.6954C2766.5794,-163.0882 2780.5392,-150.0785 2794.8276,-141 2808.445,-132.3478 2824.4889,-125.0917 2839.1773,-119.4129"/>
<polygon fill="#000000" stroke="#000000" points="2840.4424,-122.6768 2848.5949,-115.9102 2838.0021,-116.1159 2840.4424,-122.6768"/>
<text text-anchor="middle" x="2868.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel4 -->
<g id="node49" class="node">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="252.8276" cy="-627" rx="252.6553" ry="18"/>
<text text-anchor="middle" x="252.8276" y="-623.3" font-family="Times,serif" font-size="14.00" fill="#000000">_10xVisiumSpatialTranscriptomics_RNA_seqLevel4</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_RNA_seqLevel4&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel3 -->
<g id="edge7" class="edge">
<title>_10xVisiumSpatialTranscriptomics_RNA_seqLevel4&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel3</title>
<path fill="none" stroke="#000000" d="M252.8276,-608.9735C252.8276,-597.1918 252.8276,-581.5607 252.8276,-568.1581"/>
<polygon fill="#000000" stroke="#000000" points="256.3277,-568.0033 252.8276,-558.0034 249.3277,-568.0034 256.3277,-568.0033"/>
<text text-anchor="middle" x="326.8276" y="-579.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel4 -->
<g id="node50" class="node">
<title>ScRNA_seqLevel4</title>
<ellipse fill="none" stroke="#000000" cx="3253.8276" cy="-540" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="3253.8276" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel4</text>
</g>
<!-- ScRNA_seqLevel4&#45;&gt;ScRNA_seqLevel3 -->
<g id="edge6" class="edge">
<title>ScRNA_seqLevel4&#45;&gt;ScRNA_seqLevel3</title>
<path fill="none" stroke="#000000" d="M3253.8276,-521.9735C3253.8276,-510.1918 3253.8276,-494.5607 3253.8276,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="3257.3277,-481.0033 3253.8276,-471.0034 3250.3277,-481.0034 3257.3277,-481.0033"/>
<text text-anchor="middle" x="3327.8276" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- LungCancerTier3 -->
<g id="node52" class="node">
<title>LungCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="3027.8276" cy="-192" rx="92.8835" ry="18"/>
<text text-anchor="middle" x="3027.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">LungCancerTier3</text>
</g>
<!-- LungCancerTier3&#45;&gt;Patient -->
<g id="edge5" class="edge">
<title>LungCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M2999.3778,-174.8116C2975.8718,-160.6101 2942.4461,-140.4154 2917.5878,-125.3968"/>
<polygon fill="#000000" stroke="#000000" points="2919.2204,-122.294 2908.8513,-120.1185 2915.6006,-128.2854 2919.2204,-122.294"/>
<text text-anchor="middle" x="3037.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SRRSBiospecimen -->
<g id="node53" class="node">
<title>SRRSBiospecimen</title>
<ellipse fill="none" stroke="#000000" cx="3235.8276" cy="-192" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="3235.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSBiospecimen</text>
</g>
<!-- SRRSBiospecimen&#45;&gt;Patient -->
<g id="edge4" class="edge">
<title>SRRSBiospecimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M3202.248,-175.0666C3178.6272,-163.8232 3145.9766,-149.6012 3115.8276,-141 3055.9405,-123.9148 2984.8981,-114.4001 2937.3483,-109.5051"/>
<polygon fill="#000000" stroke="#000000" points="2937.5724,-106.0102 2927.2745,-108.5011 2936.8781,-112.9757 2937.5724,-106.0102"/>
<text text-anchor="middle" x="3229.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel3&#45;&gt;ScATAC_seqLevel2 -->
<g id="edge3" class="edge">
<title>ScATAC_seqLevel3&#45;&gt;ScATAC_seqLevel2</title>
<path fill="none" stroke="#000000" d="M4140.8276,-434.9735C4140.8276,-423.1918 4140.8276,-407.5607 4140.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="4144.3277,-394.0033 4140.8276,-384.0034 4137.3277,-394.0034 4144.3277,-394.0033"/>
<text text-anchor="middle" x="4214.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SRRSImagingLevel2 -->
<g id="node55" class="node">
<title>SRRSImagingLevel2</title>
<ellipse fill="none" stroke="#000000" cx="3244.8276" cy="-279" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="3244.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSImagingLevel2</text>
</g>
<!-- SRRSImagingLevel2&#45;&gt;Biospecimen -->
<g id="edge2" class="edge">
<title>SRRSImagingLevel2&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M3203.5043,-262.364C3171.6504,-250.3961 3126.1965,-235.1535 3084.8276,-228 2852.1452,-187.7645 2788.0434,-240.0492 2553.8276,-210 2547.2814,-209.1602 2540.4827,-208.0342 2533.7375,-206.7533"/>
<polygon fill="#000000" stroke="#000000" points="2534.4227,-203.3211 2523.9289,-204.781 2533.0427,-210.1837 2534.4227,-203.3211"/>
<text text-anchor="middle" x="3216.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel1 -->
<g id="node56" class="node">
<title>ScRNA_seqLevel1</title>
<ellipse fill="none" stroke="#000000" cx="3023.8276" cy="-279" rx="96.6831" ry="18"/>
<text text-anchor="middle" x="3023.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScRNA_seqLevel1</text>
</g>
<!-- ScRNA_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge1" class="edge">
<title>ScRNA_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M2986.7103,-262.3078C2958.546,-250.4771 2918.5405,-235.435 2881.8276,-228 2738.7353,-199.0213 2698.4353,-230.0937 2553.8276,-210 2547.2906,-209.0917 2540.4977,-207.922 2533.7559,-206.6155"/>
<polygon fill="#000000" stroke="#000000" points="2534.4482,-203.1847 2523.9507,-204.6178 2533.0507,-210.0438 2534.4482,-203.1847"/>
<text text-anchor="middle" x="3006.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel1 -->
<g id="node64" class="node">
<title>BulkWESLevel1</title>
<ellipse fill="none" stroke="#000000" cx="3935.8276" cy="-279" rx="86.3847" ry="18"/>
<text text-anchor="middle" x="3935.8276" y="-275.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkWESLevel1</text>
</g>
<!-- BulkWESLevel2&#45;&gt;BulkWESLevel1 -->
<g id="edge38" class="edge">
<title>BulkWESLevel2&#45;&gt;BulkWESLevel1</title>
<path fill="none" stroke="#000000" d="M3935.8276,-347.9735C3935.8276,-336.1918 3935.8276,-320.5607 3935.8276,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="3939.3277,-307.0033 3935.8276,-297.0034 3932.3277,-307.0034 3939.3277,-307.0033"/>
<text text-anchor="middle" x="4009.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- SRRSClinicalDataTier2 -->
<g id="node58" class="node">
<title>SRRSClinicalDataTier2</title>
<ellipse fill="none" stroke="#000000" cx="3469.8276" cy="-192" rx="119.6788" ry="18"/>
<text text-anchor="middle" x="3469.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">SRRSClinicalDataTier2</text>
</g>
<!-- SRRSClinicalDataTier2&#45;&gt;Patient -->
<g id="edge37" class="edge">
<title>SRRSClinicalDataTier2&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M3425.8179,-175.2446C3393.6176,-163.7034 3348.6158,-149.0496 3307.8276,-141 3238.5095,-127.32 3036.0635,-113.9846 2938.1325,-108.1163"/>
<polygon fill="#000000" stroke="#000000" points="2938.0455,-104.605 2927.8553,-107.5049 2937.6298,-111.5926 2938.0455,-104.605"/>
<text text-anchor="middle" x="3439.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel1&#45;&gt;Biospecimen -->
<g id="edge36" class="edge">
<title>ElectronMicroscopyLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M3450.6056,-262.4417C3408.554,-250.4302 3348.5748,-235.096 3294.8276,-228 2968.2312,-184.8811 2880.7773,-250.3527 2553.8276,-210 2547.1826,-209.1799 2540.279,-208.0535 2533.4362,-206.7612"/>
<polygon fill="#000000" stroke="#000000" points="2533.9846,-203.3016 2523.4914,-204.7654 2532.6072,-210.1647 2533.9846,-203.3016"/>
<text text-anchor="middle" x="3443.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- Slide_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge35" class="edge">
<title>Slide_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M3694.4288,-264.3377C3649.5721,-252.0439 3581.9447,-235.3534 3521.8276,-228 3094.7143,-175.7566 2981.0321,-261.492 2553.8276,-210 2547.1803,-209.1988 2540.2753,-208.0844 2533.4316,-206.799"/>
<polygon fill="#000000" stroke="#000000" points="2533.9782,-203.3391 2523.4859,-204.81 2532.6053,-210.2032 2533.9782,-203.3391"/>
<text text-anchor="middle" x="3675.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1 -->
<g id="edge33" class="edge">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M648.0228,-434.7449C650.4449,-406.5811 651.2147,-351.9321 626.8276,-315 623.9314,-310.6141 620.3005,-306.6824 616.2657,-303.1767"/>
<polygon fill="#000000" stroke="#000000" points="618.1717,-300.2287 608.0961,-296.9526 613.9295,-305.7969 618.1717,-300.2287"/>
<text text-anchor="middle" x="722.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- _10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2 -->
<g id="edge34" class="edge">
<title>_10xVisiumSpatialTranscriptomics_AuxiliaryFiles&#45;&gt;_10xVisiumSpatialTranscriptomics_RNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M557.7037,-436.1538C533.5452,-430.796 507.4965,-424.3286 483.8276,-417 457.5953,-408.8778 429.1635,-397.6944 405.8649,-387.8693"/>
<polygon fill="#000000" stroke="#000000" points="407.1179,-384.5988 396.5463,-383.8972 404.373,-391.0382 407.1179,-384.5988"/>
<text text-anchor="middle" x="557.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ColorectalCancerTier3 -->
<g id="node63" class="node">
<title>ColorectalCancerTier3</title>
<ellipse fill="none" stroke="#000000" cx="3724.8276" cy="-192" rx="117.7793" ry="18"/>
<text text-anchor="middle" x="3724.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">ColorectalCancerTier3</text>
</g>
<!-- ColorectalCancerTier3&#45;&gt;Patient -->
<g id="edge32" class="edge">
<title>ColorectalCancerTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M3671.3286,-175.926C3629.8504,-164.1716 3570.7164,-148.947 3517.8276,-141 3406.77,-124.3126 3070.9368,-111.3854 2938.4326,-106.8024"/>
<polygon fill="#000000" stroke="#000000" points="2938.2375,-103.2937 2928.1233,-106.4485 2937.9973,-110.2896 2938.2375,-103.2937"/>
<text text-anchor="middle" x="3665.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkWESLevel1&#45;&gt;Biospecimen -->
<g id="edge31" class="edge">
<title>BulkWESLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M3892.3803,-263.399C3855.9301,-251.1463 3802.2141,-235.0215 3753.8276,-228 3489.8953,-189.7004 2818.6647,-241.4387 2553.8276,-210 2547.1788,-209.2107 2540.2729,-208.1039 2533.4288,-206.8229"/>
<polygon fill="#000000" stroke="#000000" points="2533.9742,-203.3628 2523.4826,-204.8381 2532.6043,-210.2275 2533.9742,-203.3628"/>
<text text-anchor="middle" x="3893.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScATAC_seqLevel1&#45;&gt;Biospecimen -->
<g id="edge30" class="edge">
<title>ScATAC_seqLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M4098.5291,-262.6179C4064.8,-250.4442 4016.0505,-234.8144 3971.8276,-228 3816.0973,-204.0033 2710.3185,-228.3941 2553.8276,-210 2547.1779,-209.2184 2540.2714,-208.1165 2533.4269,-206.8382"/>
<polygon fill="#000000" stroke="#000000" points="2533.9716,-203.378 2523.4804,-204.8562 2532.6036,-210.2431 2533.9716,-203.378"/>
<text text-anchor="middle" x="4111.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ElectronMicroscopyLevel4 -->
<g id="node66" class="node">
<title>ElectronMicroscopyLevel4</title>
<ellipse fill="none" stroke="#000000" cx="3504.8276" cy="-540" rx="135.6761" ry="18"/>
<text text-anchor="middle" x="3504.8276" y="-536.3" font-family="Times,serif" font-size="14.00" fill="#000000">ElectronMicroscopyLevel4</text>
</g>
<!-- ElectronMicroscopyLevel4&#45;&gt;ElectronMicroscopyLevel3 -->
<g id="edge29" class="edge">
<title>ElectronMicroscopyLevel4&#45;&gt;ElectronMicroscopyLevel3</title>
<path fill="none" stroke="#000000" d="M3504.8276,-521.9735C3504.8276,-510.1918 3504.8276,-494.5607 3504.8276,-481.1581"/>
<polygon fill="#000000" stroke="#000000" points="3508.3277,-481.0033 3504.8276,-471.0034 3501.3277,-481.0034 3508.3277,-481.0033"/>
<text text-anchor="middle" x="3578.8276" y="-492.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Segmentation -->
<g id="node67" class="node">
<title>ImagingLevel3Segmentation</title>
<ellipse fill="none" stroke="#000000" cx="5579.8276" cy="-453" rx="145.6742" ry="18"/>
<text text-anchor="middle" x="5579.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Segmentation</text>
</g>
<!-- ImagingLevel3Segmentation&#45;&gt;ImagingLevel2 -->
<g id="edge28" class="edge">
<title>ImagingLevel3Segmentation&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M5575.9398,-434.7818C5574.7272,-424.4591 5574.9772,-411.7091 5580.8276,-402 5584.3614,-396.1354 5589.2241,-391.1551 5594.7127,-386.9445"/>
<polygon fill="#000000" stroke="#000000" points="5596.7596,-389.7861 5603.1201,-381.3129 5592.8639,-383.9703 5596.7596,-389.7861"/>
<text text-anchor="middle" x="5654.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MassSpectrometryLevel2&#45;&gt;MassSpectrometryLevel1 -->
<g id="edge27" class="edge">
<title>MassSpectrometryLevel2&#45;&gt;MassSpectrometryLevel1</title>
<path fill="none" stroke="#000000" d="M2963.9353,-349.019C2926.4957,-334.8571 2873.0248,-314.6311 2833.1706,-299.5558"/>
<polygon fill="#000000" stroke="#000000" points="2834.1982,-296.2026 2823.6067,-295.9382 2831.7216,-302.7498 2834.1982,-296.2026"/>
<text text-anchor="middle" x="2980.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Image -->
<g id="node70" class="node">
<title>ImagingLevel3Image</title>
<ellipse fill="none" stroke="#000000" cx="5868.8276" cy="-453" rx="109.6807" ry="18"/>
<text text-anchor="middle" x="5868.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">ImagingLevel3Image</text>
</g>
<!-- ImagingLevel3Image&#45;&gt;ImagingLevel2 -->
<g id="edge26" class="edge">
<title>ImagingLevel3Image&#45;&gt;ImagingLevel2</title>
<path fill="none" stroke="#000000" d="M5803.6358,-438.4996C5785.0405,-433.0746 5765.1408,-425.9856 5747.8276,-417 5738.2782,-412.0439 5738.0623,-407.5201 5728.8276,-402 5718.8173,-396.0163 5707.6317,-390.4752 5696.7944,-385.6234"/>
<polygon fill="#000000" stroke="#000000" points="5697.9655,-382.3162 5687.3989,-381.5432 5695.1771,-388.7369 5697.9655,-382.3162"/>
<text text-anchor="middle" x="5821.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel3Image&#45;&gt;ImagingLevel3Channels -->
<g id="edge25" class="edge">
<title>ImagingLevel3Image&#45;&gt;ImagingLevel3Channels</title>
<path fill="none" stroke="#000000" d="M5883.0823,-435.1028C5892.3574,-424.3788 5905.2258,-411.104 5918.8276,-402 5927.5398,-396.1687 5937.3436,-391.0297 5947.1765,-386.5948"/>
<polygon fill="#000000" stroke="#000000" points="5948.7698,-389.7197 5956.5783,-382.5588 5946.0086,-383.2873 5948.7698,-389.7197"/>
<text text-anchor="middle" x="5992.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScmC_seqLevel2 -->
<g id="node71" class="node">
<title>ScmC_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="2332.8276" cy="-366" rx="90.9839" ry="18"/>
<text text-anchor="middle" x="2332.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">ScmC_seqLevel2</text>
</g>
<!-- ScmC_seqLevel2&#45;&gt;ScmC_seqLevel1 -->
<g id="edge24" class="edge">
<title>ScmC_seqLevel2&#45;&gt;ScmC_seqLevel1</title>
<path fill="none" stroke="#000000" d="M2349.4111,-348.0492C2354.082,-342.4989 2358.9431,-336.2068 2362.8276,-330 2367.4434,-322.6247 2371.645,-314.1663 2375.1572,-306.286"/>
<polygon fill="#000000" stroke="#000000" points="2378.3831,-307.6438 2379.0808,-297.072 2371.9427,-304.9012 2378.3831,-307.6438"/>
<text text-anchor="middle" x="2444.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ClinicalDataTier2 -->
<g id="node72" class="node">
<title>ClinicalDataTier2</title>
<ellipse fill="none" stroke="#000000" cx="3953.8276" cy="-192" rx="92.8835" ry="18"/>
<text text-anchor="middle" x="3953.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">ClinicalDataTier2</text>
</g>
<!-- ClinicalDataTier2&#45;&gt;Patient -->
<g id="edge23" class="edge">
<title>ClinicalDataTier2&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M3903.4466,-176.8086C3861.2403,-164.7996 3799.1822,-148.803 3743.8276,-141 3587.2688,-118.931 3101.9471,-108.7492 2938.3249,-105.8814"/>
<polygon fill="#000000" stroke="#000000" points="2938.0786,-102.3767 2928.0195,-105.703 2937.9574,-109.3757 2938.0786,-102.3767"/>
<text text-anchor="middle" x="3892.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel2 -->
<g id="node73" class="node">
<title>BulkRNA_seqLevel2</title>
<ellipse fill="none" stroke="#000000" cx="1092.8276" cy="-366" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="1092.8276" y="-362.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel2</text>
</g>
<!-- BulkRNA_seqLevel2&#45;&gt;BulkRNA_seqLevel1 -->
<g id="edge22" class="edge">
<title>BulkRNA_seqLevel2&#45;&gt;BulkRNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M1092.8276,-347.9735C1092.8276,-336.1918 1092.8276,-320.5607 1092.8276,-307.1581"/>
<polygon fill="#000000" stroke="#000000" points="1096.3277,-307.0033 1092.8276,-297.0034 1089.3277,-307.0034 1096.3277,-307.0033"/>
<text text-anchor="middle" x="1166.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ImagingLevel1&#45;&gt;Biospecimen -->
<g id="edge21" class="edge">
<title>ImagingLevel1&#45;&gt;Biospecimen</title>
<path fill="none" stroke="#000000" d="M5681.9078,-266.2454C5670.9765,-264.1855 5659.5842,-262.3042 5648.8276,-261 5317.1566,-220.7871 5231.8163,-236.6175 4897.8276,-228 4637.4621,-221.2821 2812.5744,-239.7558 2553.8276,-210 2547.176,-209.2351 2540.2683,-208.1437 2533.4231,-206.8716"/>
<polygon fill="#000000" stroke="#000000" points="2533.9662,-203.4112 2523.4759,-204.8955 2532.6022,-210.277 2533.9662,-203.4112"/>
<text text-anchor="middle" x="5548.8276" y="-231.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- ScRNA_seqLevel2&#45;&gt;ScRNA_seqLevel1 -->
<g id="edge19" class="edge">
<title>ScRNA_seqLevel2&#45;&gt;ScRNA_seqLevel1</title>
<path fill="none" stroke="#000000" d="M3211.1054,-349.8399C3172.9801,-335.4186 3117.0315,-314.2554 3076.2178,-298.8172"/>
<polygon fill="#000000" stroke="#000000" points="3077.3021,-295.4854 3066.7106,-295.221 3074.8255,-302.0326 3077.3021,-295.4854"/>
<text text-anchor="middle" x="3225.8276" y="-318.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- BulkRNA_seqLevel3 -->
<g id="node76" class="node">
<title>BulkRNA_seqLevel3</title>
<ellipse fill="none" stroke="#000000" cx="1092.8276" cy="-453" rx="106.6812" ry="18"/>
<text text-anchor="middle" x="1092.8276" y="-449.3" font-family="Times,serif" font-size="14.00" fill="#000000">BulkRNA_seqLevel3</text>
</g>
<!-- BulkRNA_seqLevel3&#45;&gt;BulkRNA_seqLevel2 -->
<g id="edge20" class="edge">
<title>BulkRNA_seqLevel3&#45;&gt;BulkRNA_seqLevel2</title>
<path fill="none" stroke="#000000" d="M1092.8276,-434.9735C1092.8276,-423.1918 1092.8276,-407.5607 1092.8276,-394.1581"/>
<polygon fill="#000000" stroke="#000000" points="1096.3277,-394.0033 1092.8276,-384.0034 1089.3277,-394.0034 1096.3277,-394.0033"/>
<text text-anchor="middle" x="1166.8276" y="-405.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- MelanomaTier3 -->
<g id="node77" class="node">
<title>MelanomaTier3</title>
<ellipse fill="none" stroke="#000000" cx="4148.8276" cy="-192" rx="83.6854" ry="18"/>
<text text-anchor="middle" x="4148.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">MelanomaTier3</text>
</g>
<!-- MelanomaTier3&#45;&gt;Patient -->
<g id="edge18" class="edge">
<title>MelanomaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M4105.9717,-176.499C4070.3273,-164.3929 4017.9844,-148.4203 3970.8276,-141 3868.6177,-124.9169 3144.5643,-109.9835 2938.4499,-106.0214"/>
<polygon fill="#000000" stroke="#000000" points="2938.2397,-102.5168 2928.1745,-105.8247 2938.1056,-109.5155 2938.2397,-102.5168"/>
<text text-anchor="middle" x="4108.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
<!-- NeuroblastomaandGliomaTier3 -->
<g id="node78" class="node">
<title>NeuroblastomaandGliomaTier3</title>
<ellipse fill="none" stroke="#000000" cx="4407.8276" cy="-192" rx="157.0724" ry="18"/>
<text text-anchor="middle" x="4407.8276" y="-188.3" font-family="Times,serif" font-size="14.00" fill="#000000">NeuroblastomaandGliomaTier3</text>
</g>
<!-- NeuroblastomaandGliomaTier3&#45;&gt;Patient -->
<g id="edge17" class="edge">
<title>NeuroblastomaandGliomaTier3&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M4349.7729,-175.2624C4305.5301,-163.3254 4242.8762,-148.1687 4186.8276,-141 4061.9201,-125.0242 3169.2209,-109.6148 2938.2653,-105.8636"/>
<polygon fill="#000000" stroke="#000000" points="2938.1458,-102.3613 2928.0905,-105.699 2938.0325,-109.3604 2938.1458,-102.3613"/>
<text text-anchor="middle" x="4339.8276" y="-144.8" font-family="Times,serif" font-size="14.00" fill="#000000">requires_component</text>
</g>
</g>
</svg>
</div>
