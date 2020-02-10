# Recipes
<table>
	<thead>
		<tr>
			<th>Category</th>
			<th>Recipe</th>
			<th>Description</th>
			<th>Key Parameters</th>
			<th>Sample devops pipelines using the Recipe</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="5">Continuous Integration</td>
			<td>Publish a Batch Inference Pipeline</td>
			<td>Publishes a batch inference pipeline to the workspace &amp; optionally runs it</td>
			<td>
				<ul>
					<li>pipeline yml path (string)</li>
					<li>run pipeline (bool)</li>
				</ul>
			</td>
			<td>
				<ul>
					<li>
						<a href="imgs/PublishBatchInferencePipeline.png">Sample output</a>
					</li>
					<li>
						<a href="../../mlops/model_pipelines/risk-model/BatchInfForRiskModel.yml">Sample pipeline for structured data</a>
					</li>
					<li>
						<a href="../../mlops/model_pipelines/img-model/BatchInfForImgModel.yml">Sample pipeline for image data</a>
					</li>
					<ul></ul>
				</ul>
			</td>
		</tr>
		<tr>
			<td>&nbsp;Register Pretrained Model</td>
			<td>Register a pretrained model storedin the repo (supports git LFS)</td>
			<td>
				<ul>
					<li>lfs (boolean)</li>
					<li>model name</li>
					<li>model path</li>
				</ul>
				<p>Will also accept the following parameters and gracefully handle null values: model framework, framework version, sample input &amp; output dataset&nbsp;&nbsp;</p>
			</td>
			<td>
				<ul>
					<li>&nbsp;
						<a href="imgs/RegisterPretrainedModel.png">Sample output</a>
					</li>
					<li>
						<a href="../../mlops/model_pipelines/risk-model/snippets/RegisterPretrainedRiskModel.yml">Sample pipeline for structured model</a>
					</li>
					<li>
						<a href="../../mlops/model_pipelines/img-model/RegisterPretrainedImgModel.yml">Sample pipeline for DL model (images)</a>
					</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>